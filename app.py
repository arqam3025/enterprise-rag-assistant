"""Local enterprise document retrieval and optional grounded LLM demo."""
from pathlib import Path
import streamlit as st
from retrieval import load_documents, grounded_answer
from llm import ollama_answer

st.set_page_config(page_title="Enterprise RAG Assistant",layout="wide")
st.title("Enterprise Knowledge Assistant")
st.caption("Local document retrieval with optional Ollama LLM generation; sample policies are fictional.")
docs=load_documents(Path(__file__).parent/"knowledge")
st.write(f"Indexed documents: {len(docs)}")
mode=st.radio("Answer mode",["Evidence only (no LLM)","Local Ollama LLM"],horizontal=True)
model=st.text_input("Ollama model name",value="llama3.2") if mode=="Local Ollama LLM" else None
question=st.text_input("Ask about the sample service policies",value="What is the P1 response time?")
if st.button("Answer question"):
    message,matches=grounded_answer(question,docs)
    if not matches:
        st.warning(message)
    else:
        if mode=="Local Ollama LLM":
            try:
                answer=ollama_answer(question,matches,model=model)
                st.subheader("Generated answer")
                st.write(answer)
                st.caption("LLM answers may be incorrect. Check the source passages below.")
            except (RuntimeError,ValueError) as exc:
                st.error(str(exc))
                st.info("Showing retrieved evidence instead.")
        else:
            st.info(message)
        st.subheader("Retrieved supporting passages")
        for index,item in enumerate(matches,1):
            with st.expander(f"[{index}] {item['source']} · similarity {item['score']:.2f}",expanded=True):
                st.write(item["text"])
st.warning("Demo only: fictional policies, no authentication or document permissions. Never upload confidential documents.")
