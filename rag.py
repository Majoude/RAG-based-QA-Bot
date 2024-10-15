# Install necessary libraries
# !pip install pinecone-client cohere

import os
import cohere  # Or OpenAI if you prefer
from pinecone import Pinecone, ServerlessSpec
from sentence_transformers import SentenceTransformer

# Initialize Pinecone
pc = Pinecone() # This reads the PINECONE_API_KEY env var
# pinecone.init(api_key='PINECONE_API_KEY', environment='your_pinecone_environment')

# Initialize Cohere (You can replace this with OpenAI GPT or other models)
# cohere_client = cohere.Client('COHERE_API_KEY')####

# Initialize Cohere (You can replace this with OpenAI GPT or other models)
cohere_api_key = os.getenv('COHERE_API_KEY')
# Initialize Cohere client
cohere_client = cohere.Client(cohere_api_key)

# Initialize the vector store with Pinecone
index_name = 'qa-bot-index'

if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=384, # Replace with your model dimensions
        metric="cosine", # Replace with your model metric
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        ) 
    )

index = pc.Index(index_name)
print(index.describe_index_stats())
# Initialize the Sentence Transformer model for creating embeddings
embedding_model = SentenceTransformer('multi-qa-MiniLM-L6-cos-v1')  # You can choose other models as well

# Sample Dataset
documents = [
    {"id": "doc1", "text": "We offer 24/7 customer service support to our business clients."},
    {"id": "doc2", "text": "Our company was founded in 2010 and has grown to over 500 employees."},
    {"id": "doc3", "text": "We specialize in developing AI-based tools for business automation."},
]

# 1. Storing Documents in Pinecone with embeddings

def add_documents_to_pinecone(docs):
    vectors = []
    for doc in docs:
        embedding = embedding_model.encode(doc['text']).tolist()
        vectors.append((doc['id'], embedding, {"txt": "We offer 3 We offer 3 We offer 3We offer 3We offer 3We offer 3We offer 3We offer 3We offer 3We offer 3We offer 3We offer 5"}))
    
    # Upsert to Pinecone
    index.upsert(vectors, namespace="example-namespace")

add_documents_to_pinecone(documents)

# 2. Retrieve relevant documents from Pinecone based on the user's question

def retrieve_documents(query, top_k=10):
    query_embedding = embedding_model.encode(query).tolist()
    
    # Query Pinecone for top K most similar documents
    results = index.query(namespace="example-namespace", vector=[query_embedding], top_k=top_k, include_metadata=True)
    print(results)
    print([match['metadata']['txt'] for match in results['matches']])
    # Extract document IDs and their relevance scores
    retrieved_docs = []
    for match in results['matches']:
        doc_id = match['id']
        score = match['score']
        for doc in documents:
            if doc['id'] == doc_id:
                retrieved_docs.append((doc['text'], score))
    
    return retrieved_docs

# 3. Generate the final answer using the Cohere API

def generate_answer(query, retrieved_docs):
    # Combine retrieved docs and the user's query
    context = "\n".join([doc[0] for doc in retrieved_docs])
    prompt = f"Context:\n{context}\n\nQuestion:\n{query}\n\nAnswer:"

    # Use the Cohere API to generate the answer
    response = cohere_client.generate(
        model='command-xlarge-nightly',  # Use a suitable model
        prompt=prompt,
        max_tokens=150,
        temperature=0.7,
    )
    
    return response.generations[0].text.strip()

# 4. Putting it all together into a QA Bot function

def qa_bot(query):
    # Retrieve relevant documents
    retrieved_docs = retrieve_documents(query)
    
    # Generate a coherent answer based on the retrieved documents
    answer = generate_answer(query, retrieved_docs)
    
    return answer

# 5. Example Query

query = "What services does your company provide?"
answer = qa_bot(query)
print(f"Q: {query}\nA: {answer}")
