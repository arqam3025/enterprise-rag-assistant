# Enterprise RAG Knowledge Assistant

**Status:** Local retrieval app with **optional Ollama-based LLM generation**. No commercial deployment, role-based permissions or production security is claimed.

## Features

- Local fictional service/SLA knowledge documents
- TF-IDF cosine-similarity retrieval baseline and cited source excerpts
- Optional grounded text generation through a **locally running Ollama** model
- Retrieval evaluation with labelled example questions
- Tests for retrieval, prompting, no-evidence handling and local-only endpoint restriction

## Setup (Windows PowerShell)

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app.py
```

**Evidence-only mode** works without a language model or API key.

For LLM mode, separately install [Ollama](https://ollama.com/), then run:

```powershell
ollama pull llama3.2
ollama serve
```

If Ollama is already running in the background, you do not need a second `ollama serve`. Select **Local Ollama LLM** in the application.

## Test and evaluate

```powershell
python -m unittest discover -s tests -v
python evaluation.py
```

## Architecture

Sample .txt policies → TF-IDF retrieval → top source excerpts → (optional) local Ollama chat → answer + retrieved evidence.

## Limitations

- The generated answer is **not automatically fact-checked**. Displayed sources are retrieved passages; their presence does not prove that the model's claims are supported.
- A relevance score above zero is not proof of sufficient evidence. Verify responses manually.
- Retrieval uses whole documents rather than chunking or embedding search.
- No identity verification, document-level access control, audit logging, prompt-injection guarantee or production deployment.
- Local Ollama calls can require substantial RAM and model downloads; model availability depends on your machine.
- The demo only accepts the local Ollama server at port 11434 and must not be used with confidential business documents.

## Future work

Chunking and embedding retrieval, citation verification, adversarial prompt-injection tests, permission-aware search and secure deployment.
