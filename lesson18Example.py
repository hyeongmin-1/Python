import streamlit as st
st.title("오픈 대화방")
if "messages" not in st.session_state:
    st.session_state.messages = []
if st.button("대화 지우기"):
    st.session_state.messages = []
question = st.chat_input("질문")
if question and question.strip():
    st.session_state.messages += [
        {"role":"user","content":question},
        {"role":"assistant","content":f"{len(question)}"}]
    st.session_state.messages = st.session_state.messages[-10:]
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])