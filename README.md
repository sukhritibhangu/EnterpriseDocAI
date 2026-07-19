# Enterprise Document Intelligence AI

Enterprise Document Intelligence AI is a Streamlit-based Retrieval-Augmented Generation (RAG) application that allows you to upload multiple PDF documents and query them using an LLM. 

## Features

- **Multiple PDF Upload**: Upload and process multiple PDFs at once.
- **RAG Architecture**: Uses ChromaDB for vector storage and retrieval.
- **Source Citations**: AI answers include source chunks (citations) to verify accuracy.
- **Modern UI**: Chat-like interface with sidebar document management.

## Setup Instructions

1. **Clone the repository** (if applicable) or navigate to the project directory.

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables**:
   Copy `.env.example` to `.env` and add your Groq API Key:
   ```bash
   cp .env.example .env
   ```
   Open `.env` and set `GROQ_API_KEY=your_key_here`.

## Running the Application

You can use the provided startup scripts:

**Windows**:
```bash
run.bat
```

**Linux/Mac (or Bash)**:
```bash
./run.sh
```

Alternatively, run Streamlit directly:
```bash
streamlit run app.py
```

## Testing

Run tests to ensure everything is working correctly:
```bash
pytest
```
