import pandas as pd
import streamlit as st

st.title("세 과목 점수")
rows = [
    {"subject":"scrore","english":80,"math":90,"korean":100},
    {"subject":"roy","english":60,"math":50,"korean":90},
    {"subject":"emm","english":80,"math":60,"korean":30}
    
]
df = pd.DataFrame(rows)
df["revenue"] = (df["english"] + df["math"] + df["korean"]) / 3 
st.dataframe(df,hide_index=True)
st.bar_chart(df.set_index("subject")["revenue"])
st.metric("총점",f"{int(df["revenue"].sum())}점")  