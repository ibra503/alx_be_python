# Ask the user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Provide a customized reminder
match priority:
    case "high":
        if time_bound == "yes":
            print("Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print("Note: '{task}' is a high priority task. Try to complete it as soon as possible.")
    case "medium":
        if time_bound == "yes":
            print("Reminder: '{task}' is a medium priority task that requires immediate attention today!")
        else:
            print("Note: '{task}' is a medium priority task. Plan to do it soon.")
    case "low":
        if time_bound == "yes":
            print("Reminder: '{task}' is a low priority task that requires immediate attention today!")
        else:
            print("Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Note: '{task}' has an unknown priority. Please review and prioritize accordingly.")
