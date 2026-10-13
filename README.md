# Enterprise Knowledge Assistant — Retrieval Prototype

**Status:** Working local document-search baseline. This is **not yet a full RAG/LLM system**: no generative model, user authentication or production security controls have been implemented.

## Features

- Searches fictional service documentation and SLA policies.
- Returns relevant source passages and source filenames.
- Uses TF-IDF cosine similarity as a reproducible retrieval baseline.
- Abstains when no relevant document is found.
- Includes automated retrieval tests.

## Run

```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
streamlit run app.py
```

## Test

```bash
python -m unittest discover -s tests -v
```

## Planned improvements

- Chunked embeddings and vector database.
- Grounded LLM generation with citations and evaluation.
- Document-level authorisation and prompt-injection testing.
- Read-only API and deployment checks.

**All policy documents are fictional sample data.**
