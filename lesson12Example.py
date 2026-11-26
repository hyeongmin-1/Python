import streamlit as st

st.set_page_config(page_title="S27",layout="wide")
st.title("Galaxy S27")
st.markdown("새로워진 **Galaxy S27**를 만나보세요")
st.sidebar.header("S27의 모델은 4개로 출시됩니다 ")
st.sidebar.write("일반,플러스,프로,울트라가 출시됩니다!")
st.sidebar.write("일반과 플러스는 Exynos가 장착되고")
st.sidebar.write("프로와 울트라는 Snapdragon이 장착되어 출시됩니다")
left,right = st.columns(2)
with left:
    st.header("더 풍성해진 디자인을 만나보세요")
    st.write("내부공간이 확보되어 더 큰 배터리와 맥세이프가 탑재되었습니다")
with right:
    st.header("가격 안내")
    st.write("**S27 일반** 256GB/512GB은 124/150만원 출시 예정")
    st.write("**S27 플러스** 256GB/512GB은 145/179만원 출시 예정")
    st.write("**S27 프로** 256GB/512GB/1TB은 150/160/170만원 출시 예정")
    st.write("**S27 울트라** 256GB/512GB/1TB은 180/200/254만원 출시 예정")