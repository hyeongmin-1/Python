import streamlit as st

st.title("오늘의 계산")
price = 12000
quantity = 3
st.write("단가:",price)
st.write("수량:",quantity)
st.write("합계:",price * quantity)