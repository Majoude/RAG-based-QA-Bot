import streamlit as st
from pdf_processing import extract_text_from_pdf
from embedding_generation import generate_embeddings
from pinecone_operations import connect_to_pinecone_index, store_embeddings_in_pinecone
from query_handling import handle_query

# Streamlit UI
st.title("RAG-based QA Bot")

# Connect to Pinecone index. The index is fixed becuase the free plan supports only limited indexes.
pinecone_index = connect_to_pinecone_index('qa-bot-index')

# Initialize session state to store processed data
if 'processed_pdf' not in st.session_state:
    st.session_state.processed_pdf = False
if 'sentences' not in st.session_state:
    st.session_state.sentences = None
if 'embeddings' not in st.session_state:
    st.session_state.embeddings = None

# PDF Upload
pdf_file = st.file_uploader("Upload PDF Document", type=["pdf"])

if pdf_file and not st.session_state.processed_pdf:
    # Process PDF and extract text
    with st.spinner("Extracting text from PDF..."):
        extracted_text = extract_text_from_pdf(pdf_file)
        st.success("Text extraction complete!")
    
    # Generate embeddings
    with st.spinner("Generating embeddings..."):
        sentences, embeddings = generate_embeddings(extracted_text)
        st.success("Embeddings generated!")

    # Store embeddings in Pinecone
    with st.spinner("Storing embeddings in Pinecone..."):
        store_embeddings_in_pinecone(pinecone_index, sentences, embeddings)
        st.success("Embeddings stored successfully!")

    # Store the sentences and embeddings in session state
    st.session_state.sentences = sentences
    st.session_state.embeddings = embeddings
    st.session_state.processed_pdf = True  # Mark that PDF has been processed

if st.session_state.processed_pdf:
    # Input field for user queries
    query = st.text_input("Ask a question about the document:")

    if query:
        # Handle the query
        with st.spinner("Searching for an answer..."):
            answer, retrieved_sentences = handle_query(query, pinecone_index)

        # Display the answer and relevant document sections
        st.write("### Answer:")
        st.write(answer)

        st.write("### Relevant Document Sections:")
        for i, sentence in enumerate(retrieved_sentences):
            st.write(f"{i+1}. {sentence}")
