import streamlit as st

st.title('제목 - st.title')
st.header('큰 소제목 - st.header')
st.subheader('작은 소제목 - st.subheader')
st.write('글자, 숫자, 리스트 모두 OK!', 123, [1, 2, 3])
st.markdown('**굵게** *기울임* '코드'')
st.caption('회색 작은 설명 글 - st.caption')

st.info('파란 안내 상자 - st.info')
st.success('초록 성공 상자 - st.success')
st.warning('노란 경고 상자 - st.warning')
st.error('빨간 오류 상자 - st.error')
st.balloons() #풍선 애니메이션