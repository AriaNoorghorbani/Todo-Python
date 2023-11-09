from functions import get_todos, write_file, show_todo


while True:
    user_action = input('Add, Show, edit complete or Exit:')

    if user_action.startswith('add'):
        todo = user_action[4:] + '\n'

        todos = get_todos()
        todos.append(todo)
        write_file(todos)

    elif 'show' in user_action:
        todos = get_todos()

        show_todo(todos)

    elif 'edit' in user_action:
        try:
            select_todo = int(user_action[5:]) - 1
            print(todos[select_todo])

            edited_todo = input('Write edited todo: ')

            with open('todo.txt', 'w') as file:
                todos[select_todo] = edited_todo + '\n'
                file.writelines(todos)

        except ValueError:
            print('The input is not valid')
            continue
        except IndexError:
            print('The index number is not valid')
            continue

    elif user_action.startswith('complete'):
        try:
            complete_item = int(user_action[9:]) - 1
            # completed = todos[complete_item]

            todos = get_todos()
            todo_to_remove = todos[complete_item].strip('\n')
            # print(f"{todo_to_remove} is completed")
            todos.pop(complete_item)

            # with open('todo.txt', 'w') as file:
            #     todos = file.writelines(todos)
            write_file(todos)

            show_todo(todos)
        except IndexError:
            print('The index is wrong')
            continue

    elif 'exit' in user_action:
        break

    else:
        print('Hey, You write a shit')
