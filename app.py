import os
import streamlit as st
from app.services.pdf_service import PDFService
from app.services.vector_service import VectorService
from app.services.rag_service import QAService

st.set_page_config(
    page_title="Enterprise Doc AI",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Enterprise Document Intelligence AI")
st.markdown("Upload documents and query them using our AI RAG system.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar for document management
with st.sidebar:
    st.header("Document Management")
    uploaded_files = st.file_uploader(
        "Upload PDFs",
        type="pdf",
        accept_multiple_files=True
    )

    if uploaded_files and st.button("Process Documents"):
        with st.spinner("Processing documents..."):
            for uploaded_file in uploaded_files:
                file_path = os.path.join("data", "uploads", uploaded_file.name)
                
                # Save file locally
                with open(file_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())
                
                # Extract and chunk
                text = PDFService.extract_text(file_path)
                chunks = PDFService.chunk_text(text, source=uploaded_file.name)
                
                # Add to Vector DB
                VectorService.add_documents(chunks)
                
            st.success("All documents processed successfully!")

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        
        # Display sources if available
        if "sources" in message and message["sources"]:
            with st.expander("View Sources"):
                for idx, source in enumerate(message["sources"]):
                    st.markdown(f"**Source {idx + 1} ({source['metadata'].get('source', 'Unknown')})**")
                    st.text(source["content"])

# React to user input
if prompt := st.chat_input("Ask a question about your documents"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Get assistant response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = QAService.ask(prompt)
            answer = response["answer"]
            sources = response["sources"]
            
            st.markdown(answer)
            
            if sources:
                with st.expander("View Sources"):
                    for idx, source in enumerate(sources):
                        st.markdown(f"**Source {idx + 1} ({source['metadata'].get('source', 'Unknown')})**")
                        st.text(source["content"])

    # Add assistant response to chat history
    st.session_state.messages.append({
        "role": "assistant", 
        "content": answer,
        "sources": sources
    })