
import streamlit as st

st.title('This is title')
st.header("This is header")
st.subheader("This is subheader")

items= ['item 1', 'item 2', 'item 3']
st.selectbox("This is dropdown box", items)
