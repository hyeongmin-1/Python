import streamlit as st

# 시작 시 streamlit run 파일명.py
# 더 정확하게 실행할려면 python -m streamlit run 파일명p,y --server.address 1270.0.01
# 종료시 터미널에 ctrl + c 
# 스트림릿 로컬호스트는 8501 오라클은 1521

st.set_page_config(page_title="첫 앱",layout="centered")
st.title("나의 첫 streamlit 앱")
st.write("파이썬으로 만든 웹 화면입니다")
st.write("계산 결과:",8000*3)

st.title("나의 학습 목표")
st.write("파이썬의 문법을 익힙니다")
st.write("문서를 찾는 AI앱입니다")

st.title("오늘의 계산")
price = 12000
quantity = 3
st.write("단가:",price)
st.write("수량:",quantity)
st.write("합계:",price * quantity)
