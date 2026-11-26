import streamlit as st
from common import parse_sales
# 업로드 없음 처리
# 정상 3행처리
# 잘못된 숫자 거부
# 필수 열 이름 안내
# 지금 있는 열이 product , quantity , price
st.title("정상 csv 오류 csv")
rowrow = ["product" , "quantity" , "price"] 
uploaded = st.file_uploader("CSV",type=["csv"])

if uploaded is None:
    st.info("파일.csv를 선택하세요.")
else:
    try:
        rows = parse_sales(uploaded.getvalue())
        st.dataframe(rows)
        st.success(f"{len(rows)}행을 읽었습니다")    
    except ValueError as exc:
        st.error(str(exc))
    except ValueError :
        st.error(int(rows))
        st.info("잘못된 숫자입니다")

rows = parse_sales(uploaded.getvalue())
if not rowrow:
    st.error(rowrow,"해당되는 열이 없습니다")
else:    
    st.success(f"{len(rowrow)}행입니다")
    st.dataframe(rows)
