import streamlit as st
from rag_pipeline import answer_query

st.set_page_config(page_title="Angel One Support Chatbot", layout="centered")
st.title("Angel One Support Chatbot")
st.caption("Ask me anything based on our support documentation and insurance PDFs.")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

query = st.text_input("Your question:", placeholder="e.g. What is the coverage for the silver plan?")

if st.button("Ask") and query:
    answer = answer_query(query)
    st.session_state.chat_history.append((query, answer))

for q, a in reversed(st.session_state.chat_history):
    st.markdown(f"**You:** {q}")
    st.markdown(f"**Bot:** {a}")