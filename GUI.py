import PySimpleGUI as sg

label = sg.Text('Type one To-Do')
input_box = sg.InputText(tooltip='Enter a To-Do')
add_button = sg.Button('Add')

window = sg.Window('My To-Do App', [[label], [input_box, add_button]])

window.read()
window.close()