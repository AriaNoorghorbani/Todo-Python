import streamlit as st
import functions

st.title("My To-do App")
st.subheader("Hello")

todos = functions.get_todos()

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Write your todo")
