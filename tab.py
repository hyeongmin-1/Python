import streamlit as st

tab1, tab2, tab3 = st.tabs(["신규","재가입자","기존 회원"])
with tab1:
    st.subheader("신규")
   
with tab2:
    st.subheader("재가입자")    
    
with tab3:
    st.subheader("기존 회원")
    