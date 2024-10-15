from sentence_transformers import SentenceTransformer
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Initialize the SentenceTransformer model globally to avoid re-loading
embedding_model = SentenceTransformer('multi-qa-MiniLM-L6-cos-v1')

def generate_embeddings(text):
    """
    Generates sentence embeddings from a text using SentenceTransformer.

    Parameters:
    text (str): Text to be split and embedded.

    Returns:
    tuple: A list of sentences and their corresponding embeddings.
    """
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,  # 500 is maximum for 'multi-qa-MiniLM-L6-cos-v1'
        chunk_overlap=50  # Set the overlap between chunks
    )

    # Split the text using LangChain's text splitter
    chunks = text_splitter.split_text(text)

    sentences = [doc.replace("\n"," ") for doc in chunks]

    embeddings = embedding_model.encode(sentences)
    return sentences, embeddings
