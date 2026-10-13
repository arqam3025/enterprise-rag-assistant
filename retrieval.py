"""Dependency-light document retrieval with TF-IDF baseline."""
from pathlib import Path
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def load_documents(folder="knowledge"):
    root=Path(folder)
    docs=[]
    for path in sorted(root.glob("*.txt")):
        text=path.read_text(encoding="utf-8").strip()
        if text:
            docs.append({"source":path.name,"text":text})
    return docs

def retrieve(question, documents, k=3):
    if not documents or not question.strip():
        return []
    corpus=[d["text"] for d in documents]
    matrix=TfidfVectorizer(stop_words="english").fit_transform(corpus+[question])
    scores=cosine_similarity(matrix[-1],matrix[:-1]).ravel()
    order=sorted(range(len(scores)),key=lambda i:(-scores[i],i))
    return [{**documents[i],"score":float(scores[i])} for i in order[:k] if scores[i]>0]

def grounded_answer(question, documents):
    """Extractive evidence only: never invent an LLM answer."""
    matches=retrieve(question,documents)
    if not matches:
        return "No supporting document found. Do not rely on an unsupported answer.",[]
    return "Relevant source passages (not an LLM-generated answer):",matches
