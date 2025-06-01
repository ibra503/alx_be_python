Task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time = input("Is it time-bound? (yes/no): ").lower()

match priority:


if priority == "high" and time == "yes":
     print ("Finish", Task, "is a high priority task that requires immediate attention today!")
elif priority == "low" and time == "no":
     print ("Note: ", Task,  "is a low priority task. Consider completing it when you have free time. ")




else:
      print("ops!")













