from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import BedrockEmbeddings
import os

bedrock_client = boto3.client(service_name="bedrock-runtime")
embeddings = BedrockEmbeddings(model_id="amazon.titan-embed-text-v1", client=bedrock_client)

def initialize_vector_store(documents):
    vectorstore = FAISS.from_documents(documents, embeddings)
    vectorstore.save_local(index_name="valorant_csv_faiss", folder_path="/tmp/")
    
def load_vector_store(index_name):
    return FAISS.load_local(index_name=index_name, folder_path="/tmp/", embeddings=embeddings, allow_dangerous_deserialization=True)
