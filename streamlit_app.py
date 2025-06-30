# Chapter 1
import streamlit as st
from datetime import date
import pandas as pd

st.title('This is title')
st.header("This is header")
st.subheader("This is subheader")

items= ['item 1', 'item 2', 'item 3']
select_item = st.selectbox("This is dropdown box", items)

st.success(f"You've select {select_item}!")

# Chapter 2
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

dob = st.date_input("Select Date", min_value= date(1995, 6, 29))
st.write(f"Your date of birth : {dob}")

today = date.today()
age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
st.write(f"Your age is: {age}")

# Chapter 3
col1, col2 = st.columns(2)

with col1:
  st.subheader("Column 1")

with col2:
  st.subheader("Column 2")

st.image("""https://images.pexels.com/photos/32117500/pexels-photo-32117500.jpeg?_gl=1*3rw2uj*_ga*NjgzMTcxMTg1LjE3NTEyODgyMTE.*_ga_8JE65Q40S6*czE3NTEyODgyMTEkbzEkZzEkdDE3NTEyODgyNTkkajEyJGwwJGgw""", width=200)

sidebar_items = st.sidebar.selectbox("This is dropdown box", items)
st.sidebar.write(f"You've select {sidebar_items}!")

st.sidebar.slider("This is a slider", 0,10,5)
st.sidebar.checkbox("This is a checkbox",items)
st.sidebar.radio('Radio button', items)

sidebar_text = st.sidebar.text_input("This is text input")
if sidebar_text:
  st.sidebar.write(f"Your test: {sidebar_text}!")

with st.expander("This is an expander"):
  st.write(
    """
    1. Line one
    2. Line two
    3. Line three
    """
  )

# Chapter 4
st.file_uploader("Upload your file", type= ['csv'])

df = pd.read_csv("https://raw.githubusercontent.com/hiteshchoudhary/Streamlit-course/refs/heads/master/chai_sales.csv")


with st.expander("Show Dataframe"):
  st.dataframe(df)
  show_stats = st.checkbox("Show Summary Stats")
  
  if show_stats:
    st.write(df.describe())











