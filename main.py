import streamlit as st

색 = st.color_picker("병아리에게 입힐 색을 골라 보세요", "#FFD400")
st.markdown(f"<h3 style='color:{색}'>이 색 옷을 입은 병아리, 어때요?</h3>", unsafe_allow_html=True)
