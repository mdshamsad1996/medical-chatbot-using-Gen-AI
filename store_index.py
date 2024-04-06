import os
from dotenv import load_dotenv
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone
from src.helper import download_hugging_face_embeddings, load_pdf,text_split


load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')

extracted_data = load_pdf("data/")
text_chunk = text_split(extracted_data)
embeddings= download_hugging_face_embeddings()


pc = Pinecone(api_key=PINECONE_API_KEY)

index_name="medical-chatbot"

# Creating Embeddings for Each of The Text Chunks & storing
docsearch = PineconeVectorStore.from_documents(text_chunk, embeddings, index_name=index_name)

