import pandas as pd
import streamlit as st

st.title("상품별 매출")
rows = [
    {"product":"book","quantity":2,"price":12000},
    {"product":"pen","quantity":5,"price":1500}
]
df = pd.DataFrame(rows)
df["revenue"] = df["quantity"] * df["price"]

# hide_index = True를 하면 행의 번호가 사라짐 없애면 행의 번호 확인가능
# st.dataframe 메서드를 사용하면 표 형태로 나옴
st.dataframe(df,hide_index=True)

# st.bar_chart(a.set_index("n")["x"])를 하면 선택한 n의 x 열 기준으로 차트짜줌
st.bar_chart(df.set_index("product")["revenue"])
st.metric("총매출",f"{int(df['revenue'].sum()):,}원")