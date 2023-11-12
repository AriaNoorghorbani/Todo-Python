import streamlit as st
import functions

todos = functions.get_todos()

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=index)
    if checkbox:
        todos.pop(index)
        functions.write_file(todos)
        del st.session_state[todo]
        st.rerun()

def add_todo():
    new_todo = st.session_state["new_todo"]
    todos.append(new_todo + "\n")
    functions.write_file(todos)



st.title("Todo App")
st.text_input(label="", placeholder="Write yout todo", on_change=add_todo, key="new_todo")

st.session_state
