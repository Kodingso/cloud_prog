import time

# List to store the tasks
tasks = []

# Function to add tasks
def add_task():
    task_name = input("Enter task name: ")
    
    try:
        task_time = int(input("Enter task time (in seconds): "))
    except ValueError:
        print("Invalid time format. Please enter a valid integer.")
        return
    
    task = {"name": task_name, "time": task_time}
    tasks.append(task)
    print("Task added successfully!")

# Function to run the task scheduler
def run_scheduler():
    print("\nTask scheduler started!")

    while tasks:
        task = tasks.pop(0)  # Remove and get the first task
        print(f"Running task: {task['name']}")

        time.sleep(task['time'])
        
        print(f"Task {task['name']} completed!")

    print("No more tasks to run.")

# Main function with menu
def main():
    while True:
        print("\nMenu:")
        print("1. Add a task")
        print("2. Run scheduler")
        print("3. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            run_scheduler()
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")


# Run the program
if __name__ == "__main__":
    main()
