import streamlit as st
st.title("range(1,n+1)")
@st.cache_data(ttl=60)
def sumadd(n):
    return sum(range(1,n+1))

n = st.number_input("숫자 입력",min_value=1,value=1)
with st.spinner("계산 중"):
    result = sumadd(int(n))
st.metric("더한 값",result)
if st.button("이 함수 캐시 지우기"):
    sumadd.clear()
    st.success("캐시를 지웠습니다")

