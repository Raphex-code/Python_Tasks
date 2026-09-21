def todo_app():
    tasks = []

    while True:
        print('\n========================')
        print('     TO-DO LIST MENU    ')
        print('========================')
        print('1. Add new Task')
        print('2. View All Task')
        print('3. Remove a Task')
        print('4. Exit')
        print('\n========================')

        choice = input('What do you want to do: ').strip()

        if choice == '1':
            new_task = input('\nEnter a new task: ').strip()
            if new_task != '':
                tasks.append(new_task)
                print(f"Success!: '{new_task}' added.")
            else:
                print("Error: Task cannot be Empty.")

        elif choice == '2':
            print('\n--- CURRENT TASKS ---')
            if len(tasks) == 0:
                print('No tasks found.')
            else:
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")

        elif choice == '3':
            print('\n--- REMOVE A TASK ---')
            if len(tasks) == 0:
                print('No tasks available to remove.')
            else:
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")

                task_num = input('\nEnter task number to remove: ').strip()
                if task_num.isdigit():
                    task_index = int(task_num) - 1

                    if 0 <= task_index < len(tasks):
                        removed = tasks.pop(task_index)
                        print(f"Success!: '{removed}' removed")
                    else:
                        print("Error: Number out of range.")
                else:
                    print("Error: Enter digits only. ")

        elif choice == '4':
            print('\nClosing Application...')
            print('\nGoodbye!')
            break

        else:
            print('\nInvalid choice. Pick between 1 and 4.')


if __name__ == "__main__":
    todo_app()
