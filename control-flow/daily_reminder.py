Task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        if time == "yes":
            print(f"Finish '{Task}' - it's a high priority task that requires immediate attention today!")
        else:
            print(f"Task '{Task}' is high priority but not urgent.")
    case "medium":
        if time == "yes":
            print(f"'{Task}' is a medium priority task with a deadline. Schedule accordingly.")
        else:
            print(f"'{Task}' is a medium priority task.")
    case "low":
        if time == "yes":
            print(f"'{Task}' is low priority but still needs to be done on time.")
        else:
            print(f"Note: '{Task}' is a low priority task. Consider doing it when you have free time.")
    case _:
        print("Invalid priority entered.")













