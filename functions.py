FILEPATH = 'todos.txt'


def get_todos(file_path=FILEPATH):
    with open(file_path, 'r') as local_file:
        local_todos = local_file.readlines()
        return local_todos


def write_file(todos, file_path = FILEPATH):
    with open(file_path, 'w') as local_file:
        local_file.writelines(todos)


def show_todo(todos):
    for index, item in enumerate(todos):
        new_item = item.strip('\n')
        print(f"{index + 1}. {new_item}")

def complete_todo(todos, todo):
    for item in todos:
        if item == todo:
            todos.remove(item)