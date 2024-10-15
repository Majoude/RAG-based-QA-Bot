import cohere
import os
from embedding_generation import embedding_model

# Initialize the Cohere client
cohere_api_key = os.getenv('COHERE_API_KEY')
# Initialize Cohere client
cohere_client = cohere.Client(cohere_api_key)

def handle_query(query, pinecone_index, top_k=3):
    """
    Handles the user query by retrieving relevant document segments and generating a response.

    Parameters:
    query (str): The user's question.
    pinecone_index (Index): The Pinecone index object.
    top_k (int): The number of top results to retrieve.

    Returns:
    tuple: Generated answer and the retrieved document segments.
    """
    query_embedding = embedding_model.encode(query).tolist()

    # Query Pinecone to retrieve relevant document segments
    results = pinecone_index.query(namespace="namespace", vector=[query_embedding], top_k=top_k, include_metadata=True)
    print(results)
    retrieved_sentences = [match['metadata']['text'] for match in results['matches']]

    # Prepare the prompt for the language model (Cohere)
    prompt = "\n\n".join(retrieved_sentences) + f"\n\nAnswer the following question based on the above content while strictly keeping your response under 150 tokens: {query}"

    # Use Cohere to generate a response
    response = cohere_client.generate(
        prompt=prompt,
        max_tokens=150
    )

    return response.generations[0].text, retrieved_sentences
