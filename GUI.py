import PySimpleGUI as sg
import time
from functions import get_todos, write_file

sg.theme('black')

clock = sg.Text(time.strftime("%b %d, %Y %H:%M:%S"), key="time")
label = sg.Text('Type one To-Do')
input_box = sg.InputText(tooltip='Enter a To-Do', key="todo")
add_button = sg.Button(size=10, image_source="images/add.png", mouseover_colors="LightBlue2", key="Add")
todo_list = sg.Listbox(values=get_todos(), key="todos", enable_events=True, size=[40, 10])
edit_button = sg.Button('Edit')
complete_button = sg.Button(key='Complete', image_source="images/complete.png", mouseover_colors="LightBlue2")
exit_button = sg.Button('Exit')

window = sg.Window('My To-Do App',
                   [
                    [clock],
                    [label],
                    [input_box, add_button],
                    [todo_list, edit_button, complete_button],
                    [exit_button]],
                   font=('Helvetica', '18'))


while True:
    event, value = window.read(timeout=1000)
    window['time'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    # print(event)
    # print(value)
    match event:
        case "Add":
            todos = get_todos()
            todo = value['todo']
            match todo:
                case "":
                    sg.popup("Please enter a todo", font=["Helvetica", "17"])
                    continue
            todos.append(todo + "\n")
            write_file(todos)
            window['todos'].update(todos)
        case "Edit":
            try:
                todo = value['todos'][0]
                todos = get_todos()
                todo_to_edit = todos.index(todo)
                todos[todo_to_edit] = value['todo'] + "\n"
                write_file(todos)
                window['todos'].update(todos)
            except IndexError:
                sg.popup("Please chose a todo", font=["Helvetica", "17"])
                continue
        case "todos":
            window['todo'].update(value=value['todos'][0])
        case "Complete":
            try:
                completed_todo = value['todo']
                todos = get_todos()
                todos.remove(completed_todo)
                write_file(todos)
                window['todos'].update(todos)
                window['todo'].update('')
            except ValueError:
                sg.popup("Please choose a correct one", font=["Helvetica", "17"])
                continue
        case "Exit":
            exit()
        case sg.WINDOW_CLOSED:
            break

window.close()