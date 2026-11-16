import streamlit as st

귀염 = st.slider("🐤 병아리 귀염지수에 투표해 주세요", 0, 100, 80)
st.write(f"이 병아리의 귀염지수는 {귀염}점!")
