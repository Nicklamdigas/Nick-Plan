tasks = []

def show_list(tasks_list):
    for index,task in enumerate(tasks_list, start=1):
        #status = "[X]" if task["done"] else"[ ]"
        print(f"{index}. {task}")

def saves_tasks(tasks_list):
        with open('tasks.txt', 'w') as file:
            for task in tasks_list:
                file.write(f"{task}\n")
def main():
    with open('tasks.txt', 'r') as file:
        for line in file.readlines():
            tasks.append(line.strip())

    while True:
        user_input = input("What would you like to do (add, list, delete, exit)?" ).lower().strip()
        if user_input in ('add'):
            user_input_add = input("Enter the task: ")
            tasks.append(user_input_add)
            saves_tasks(tasks)
            show_list(tasks)

        elif user_input in ('list'):
            show_list(tasks)
        elif user_input in ('delete'):
            show_list(tasks)
            user_input_delete = input("Enter the task index: ")
            delete_task = int(user_input_delete)
            tasks.pop(delete_task - 1)
            saves_tasks(tasks)
            print("Task deleted")
        elif user_input in ('exit'):
            break

if __name__ == "__main__":
    main()