
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

radio_item = st.radio('Radio button', items)
st.write(f"You've select {radio_item}!")

st.slider('This is slider', 0,10,5)

st.number_input("This is number input", min_value= 0, max_value= 10)

name= st.text_input("This is text input:")
if name:
        st.write(f"This is your text: {name}")

dob = st.date_input("Select Date", min_value= "1995/06/29")
st.write(f"Your date of birth : {dob}")
