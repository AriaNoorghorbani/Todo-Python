import streamlit as st
import functions

todos = functions.get_todos()

for todo in todos:
    st.checkbox(todo)
def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo + "\n")
    functions.write_file(todos)

st.title("Todo App")
st.text_input(label="", placeholder="Write yout todo", on_change=add_todo, key="new_todo")