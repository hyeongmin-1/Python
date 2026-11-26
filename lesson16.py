import streamlit as st
# Session은 서버프로그램
# 유일한 클라이언트 프로그램은 자바스크립트
# 서버 저장값을 유지시키는 명령어를 넣지 않으면
# 서버를 다시 키커나 주소를 복사해서 재실행하거나 새로고침하면 값은 초기화됨

st.title("세션 카운터")
if "count" not in st.session_state:
    st.session_state.count = 0
if st.button("증가"):
    st.session_state.count += 1
if st.button("초기화"):
    st.session_state.count = 0
st.metric("현재 값",st.session_state.count)