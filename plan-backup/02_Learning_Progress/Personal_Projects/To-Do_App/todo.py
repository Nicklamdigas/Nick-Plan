tasks = []
def show_list(tasks_list):
    for index,task in enumerate(tasks_list, start=1):
        print(f"{index}. {task}")
def main ():
    while True:
        user_input = input("What would you like to do (add, list, delete, exit)?" ).lower().strip()
        if user_input in ('add'):
            user_input_add = input("Enter the task: ")
            tasks.append(user_input_add)
            show_list(tasks)

        elif user_input in ('list'):
            show_list(tasks)
        elif user_input in ('delete'):
            show_list(tasks)
            user_input_delete = input("Enter the task index: ")
            delete_task = int(user_input_delete)
            tasks.pop(delete_task - 1)
            print("Task deleted")
        elif user_input in ('exit'):
            break

if __name__ == "__main__":
    main()