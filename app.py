import streamlit as st
from retrieval import load_documents, grounded_answer
st.set_page_config(page_title="Enterprise Knowledge Search")
st.title("Enterprise Knowledge Assistant")
st.caption("Cited document retrieval prototype; LLM answer generation is not implemented.")
docs=load_documents()
st.write(f"Indexed documents: {len(docs)}")
question=st.text_input("Ask about the sample service policies",value="What is the P1 response time?")
if st.button("Find supporting sources"):
    message,results=grounded_answer(question,docs)
    st.write(message)
    for item in results:
        with st.expander(f"{item['source']} · relevance {item['score']:.2f}",expanded=True):
            st.write(item["text"])
st.warning("Sample policies are fictional. Do not use them for operational decisions.")
