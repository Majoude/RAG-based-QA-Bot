from pinecone import Pinecone, ServerlessSpec

# Initialize Pinecone
pc = Pinecone()

def connect_to_pinecone_index(index_name, dimension=384):
    """
    Connect to a Pinecone index. Create one if it doesn't exist.

    Parameters:
    index_name (str): The name of the index.
    dimension (int): The dimensionality of the vectors.

    Returns:
    Index: The connected Pinecone index.
    """

    if index_name not in pc.list_indexes().names():
        pc.create_index(
            name=index_name,
            dimension=dimension, # Replace with your model dimensions
            metric="cosine", # Replace with your model metric
            spec=ServerlessSpec(
                cloud="aws",
                region="us-east-1",
            )
        )

    return pc.Index(index_name)


def store_embeddings_in_pinecone(index, sentences, embeddings):
    """
    Store sentences and their embeddings in Pinecone.

    Parameters:
    index (Index): The Pinecone index object.
    sentences (list): List of sentences.
    embeddings (list): List of corresponding embeddings.
    """

    # Deleting any previous data in the namespace from past documents
    if "namespace" in index.describe_index_stats()['namespaces']:
        index.delete(delete_all=True, namespace="namespace")

    # Forming the vector that will be upserted to the index with the metadata being the original text from the document
    vectors = [{"id": f"doc_{i}", "values": embeddings[i], "metadata": {"text": sentences[i]}} for i in range(len(embeddings))]


    index.upsert(vectors, namespace="namespace")
