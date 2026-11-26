import streamlit as st

st.title("단가,수량 사칙연산")
price = st.number_input("단가",min_value=1000,max_value=10000,value=1000)
quantity = st.number_input("수량",min_value=1,max_value=10000,value=1)
left,left1,right,right1 = st.columns(4)
with left:
    plus = price + quantity
    st.metric("더하기",f"{plus:,}원")
with left1:    
    minus = price - quantity
    st.metric("빼기",f"{minus:,}원")
with right:
    add = price * quantity
    st.metric("곱하기",f"{add:,}원")
with right1:    
    divide = price / quantity
    st.metric("나누기",f"{divide:,}원")

total = plus + minus + add + divide
st.metric("사칙연산 다 더한 값",f"{total:,}원")

