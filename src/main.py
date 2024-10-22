import boto3
import streamlit as st
import uuid
import os
from utilities.process_csv import process_csv_for_vectorization
from utilities.model_loader import get_trained_model, handle_llm_interaction
from utilities.s3_handler import upload_to_s3, download_from_s3
from utilities.vector_store import initialize_vector_store, load_vector_store

BUCKET_NAME = "vct-hackthon-csv-data"
VECTOR_STORE_KEY_FAISS = "valorant_csv_faiss_data/index_valorant.faiss"
VECTOR_STORE_KEY_PKL = "valorant_csv_faiss_data/index_valorant.pkl"

def get_unique_id():
    return str(uuid.uuid4())

def admin_interface():
    st.title("VALORANT CSV Data Vectorization - Admin Panel")
    uploaded_file = st.file_uploader("Upload your game data CSV", "csv")
    
    if uploaded_file is not None:
        request_id = get_unique_id()
        saved_file_name = f"{request_id}.csv"
        process_csv_for_vectorization(uploaded_file, saved_file_name)
        
        st.write("Uploading vector store to S3...")
        upload_to_s3(BUCKET_NAME, VECTOR_STORE_KEY_FAISS, VECTOR_STORE_KEY_PKL)
        st.success("Vector store uploaded successfully!")

def client_interface():
    st.title("Query the Fine-Tuned VALORANT LLM (CSV Data)")
    
    st.write("Downloading vector store from S3...")
    download_from_s3(BUCKET_NAME, VECTOR_STORE_KEY_FAISS, VECTOR_STORE_KEY_PKL)
    
    faiss_index = load_vector_store("valorant_csv_faiss")
    st.write("Vector store loaded. You can now query the fine-tuned LLM.")
    
    question = st.text_input("Ask your question about the game data:")
    
    if st.button("Query Model"):
        llm = get_trained_model()
        with st.spinner("Processing your query..."):
            response = handle_llm_interaction(llm, faiss_index, question)
            st.write(response)
        st.success("Query completed!")

def main():
    st.sidebar.title("Navigation")
    options = ["Admin", "Client"]
    choice = st.sidebar.selectbox("Select Option", options)
    
    if choice == "Admin":
        admin_interface()
    elif choice == "Client":
        client_interface()

if __name__ == "__main__":
    main()
