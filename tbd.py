from pinecone import Pinecone, ServerlessSpec

# Initialize Pinecone
pc = Pinecone()
index=pc.Index('qa-bot-index')
index.DescribeIndexStats()
print(pc.list_indexes()) 