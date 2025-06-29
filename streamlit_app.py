
import streamlit as st

st.title('This is title')
st.header("This is header")
st.subheader("This is subheader")

items= ['item 1', 'item 2', 'item 3']
select_item = st.selectbox("This is dropdown box", items)

st.success(f"You've select {select_item}!")

if st.button('button'):
  st.write('you\'ve clicked the button')

if st.checkbox('Check me'):
  st.write('you\'ve checked an item')

st.radio('Radio button', items)
