from fastapi import FastAPI, HTTPException
import cohere
import pinecone
from sentence_transformers import SentenceTransformer

# Initialize Pinecone
pinecone.init(api_key='your_pinecone_api_key', environment='your_pinecone_environment')

# Initialize Cohere
cohere_client = cohere.Client('your_cohere_api_key')

# Initialize the vector store with Pinecone
index_name = 'qa-bot-index'
if index_name not in pinecone.list_indexes():
    pinecone.create_index(index_name, dimension=768)

index = pinecone.Index(index_name)

# Initialize the Sentence Transformer model
embedding_model = SentenceTransformer('multi-qa-MiniLM-L6-cos-v1')

# Sample documents (replace this with your actual dataset)
documents = [
    {"id": "doc1", "text": "We offer 24/7 customer service support to our business clients."},
    {"id": "doc2", "text": "Our company was founded in 2010 and has grown to over 500 employees."},
    {"id": "doc3", "text": "We specialize in developing AI-based tools for business automation."},
]

# Store documents in Pinecone (similar to the previous code)
def add_documents_to_pinecone(docs):
    vectors = []
    for doc in docs:
        embedding = embedding_model.encode(doc['text']).tolist()
        vectors.append((doc['id'], embedding))
    index.upsert(vectors)

# Add sample documents to Pinecone
add_documents_to_pinecone(documents)

# Retrieve relevant documents from Pinecone
def retrieve_documents(query, top_k=3):
    query_embedding = embedding_model.encode(query).tolist()
    results = index.query(queries=[query_embedding], top_k=top_k)
    
    retrieved_docs = []
    for match in results['matches']:
        doc_id = match['id']
        for doc in documents:
            if doc['id'] == doc_id:
                retrieved_docs.append(doc['text'])
    
    return retrieved_docs

# Generate answer using Cohere API
def generate_answer(query, retrieved_docs):
    context = "\n".join(retrieved_docs)
    prompt = f"Context:\n{context}\n\nQuestion:\n{query}\n\nAnswer:"
    response = cohere_client.generate(
        model='command-xlarge-nightly',
        prompt=prompt,
        max_tokens=150,
        temperature=0.7,
    )
    
    return response.generations[0].text.strip()

# FastAPI app
app = FastAPI()

# API endpoint to handle questions
@app.post("/ask")
async def ask_question(query: str):
    try:
        retrieved_docs = retrieve_documents(query)
        if not retrieved_docs:
            return {"answer": "Sorry, I couldn't find relevant information."}

        answer = generate_answer(query, retrieved_docs)
        return {"answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Running with: uvicorn main:app --reload
