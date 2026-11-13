import streamlit as st

count = 0

if st.button('+1'):
    count += 1

st.write('누른 횟수 :', count)