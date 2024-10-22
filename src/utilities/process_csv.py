import os
import csv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from utilities.vector_store import initialize_vector_store

def process_csv_for_vectorization(uploaded_file, saved_file_name):
    with open(saved_file_name, mode="wb") as f:
        f.write(uploaded_file.getvalue())
    
    rows = []
    with open(saved_file_name, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            rows.append(" ".join(row))  # Combine columns to simulate document text

    documents = [{"content": row} for row in rows]

    chunk_size = int(os.getenv("CHUNK_SIZE", 1024))
    overlap = int(os.getenv("OVERLAP", 200))
    
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=overlap)
    splitted_docs = splitter.split_documents(documents)
    
    initialize_vector_store(splitted_docs)
