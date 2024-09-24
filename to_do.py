def main():
    # Initialize an empty list to store tasks
    tasks = []

    # Start an infinite loop to display the menu
    while True:
        print("\n***** To-Do List *****")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark Task as Done")
        print("4. Update Task")
        print("5. Exit")
        
        # Get user choice
        choice = input("Enter your choice: ")
        
        # Option 1: Add Task
        if choice == '1':
            print()
            # Get the number of tasks to add
            n_tasks = int(input("How many tasks do you want to add? "))
            for i in range(n_tasks):
                # Prompt for task input
                task = input("Enter the task: ")
                # Append the new task as a dictionary with 'done' status
                tasks.append({"task": task, "done": False})
                print("Task added!")

        # Option 2: Show Tasks
        elif choice == '2':
            print("\nTasks:")
            # Check if there are any tasks
            if not tasks:
                print("No tasks available.")
            else:
                # Enumerate through tasks to display each one with its status
                for index, task in enumerate(tasks):
                    status = "Done" if task["done"] else "Not Done"
                    print(f"{index + 1}. {task['task']} - {status}")

        # Option 3: Mark Task as Done
        elif choice == '3':
            # Prompt for the task number to mark as done
            task_index = int(input("Enter the task number to mark as done: ")) - 1
            # Check if the index is valid
            if 0 <= task_index < len(tasks):
                tasks[task_index]["done"] = True  # Mark the task as done
                print("Task marked as done!")
            else:
                print("Invalid task number.")

        # Option 4: Update Task
        elif choice == '4':
            # Prompt for the task number to update
            task_index = int(input("Enter the task number to update: ")) - 1
            # Check if the index is valid
            if 0 <= task_index < len(tasks):
                new_task = input("Enter the new task description: ")
                tasks[task_index]["task"] = new_task  # Update the task description
                print("Task updated!")
            else:
                print("Invalid task number.")

        # Option 5: Exit the program
        elif choice == '5':
            print("Exiting the To-Do list.")
            break  # Exit the loop

        # Handle invalid choices
        else:
            print("Invalid choice. Please try again.")

# Entry point of the program
if __name__ == "__main__":
    main()

