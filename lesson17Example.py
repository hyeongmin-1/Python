import streamlit as st

st.title("참가 신청")
with st.form("order_form"):
    email = st.text_input("Email")
    raw = st.text_input("참가 인원",value=1)
    submit = st.form_submit_button("신청하기")
if submit:
    st.session_state.pop("result",None)
    st.session_state.pop("result1",None)
    try:
        quantity = int(raw)
        if "@" not in email or not 1 <= quantity <= 10:
            raise ValueError("@과 인원 1~10명을 확인하세요")
        st.session_state.result = raw
        st.session_state.result1 = email
    except ValueError:
        st.error("@과 인원 1~10명을 확인하세요")
if "result1" in st.session_state:
    st.metric("신청자 이메일",f"{st.session_state.result1}")
if "result" in st.session_state:
    st.metric("신청 인원",f"{st.session_state.result}명")

