import PySimpleGUI as sg
from functions import get_todos, write_file

label = sg.Text('Type one To-Do')
input_box = sg.InputText(tooltip='Enter a To-Do', key="todo")
add_button = sg.Button('Add')
todo_list = sg.Listbox(values=get_todos(), key="todos", enable_events=True, size=[45, 10])
edit_button = sg.Button('Edit')

window = sg.Window('My To-Do App',
                   [[label], [input_box, add_button], [todo_list, edit_button]], font=('Helvetica', '20'))


while True:
    event, value = window.read()
    print(event)
    print(value)
    match event:
        case "Add":
            todos = get_todos()
            todo = value['todo']
            todos.append(todo + "\n")
            write_file(todos)
            window['todos'].update(todos)
        case "Edit":
            todo = value['todos'][0]
            todos = get_todos()
            todo_to_edit = todos.index(todo)
            todos[todo_to_edit] = value['todo'] + "\n"
            write_file(todos)
            window['todos'].update(todos)
        case "todos":
            window['todo'].update(value=value['todos'][0])
        case sg.WINDOW_CLOSED:
            break

window.close()