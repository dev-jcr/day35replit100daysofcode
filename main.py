import os, time

# Color change subroutine
def c(color):
  if color=="red":
    return ("\033[31m")
  elif color=="white":
    return ("\033[0m")
  elif color=="blue":
    return ("\033[34m")
  elif color=="yellow":
    return ("\033[33m")
  elif color == "green":
    return ("\033[32m")
  elif color == "purple":
    return ("\033[35m")

# To-Do List
tasks = []

# Title
title = f"{c('purple')}My To-Do list\n"
print(f"{title:^35}")

# First use
print(f"{c('white')}Add the first task...\n")
task = input()
print()
tasks.append(task)
print()
print("First task added!")
print()
time.sleep(1)
os.system("clear")

# Action

while True:
  action = input(f"""
  {c('white')}What do you want to do with your tasks?
  {c('yellow')}
  1. View
  2. Add
  3. Remove
  4. Edit
  5. Nuke the whole to-do list ⚠️
  {c('white')}
  """)

  # Show tasks
  if action == "1":
    for i in tasks:
      print()
      print(f"{i}")
      print("---")
      continue
      
  # Add task 
  elif action == "2":
    print()
    print(f"{c('white')}Write your new task...")
    print()
    task = input()
    counter = 0
    for i in range(len(tasks[counter])):
      if task == tasks[counter]:
        print()
        print("The task is already on the list you dummy!")
        print()
        counter += 1
      else:
        tasks.append(task)
        print()
        print("Task added!")
        print()
    time.sleep(1)
    os.system("clear")

  # Remove task
  elif action == "3":
    print()
    print(f"{c('white')}Which one you want to delete?")
    print()
    n = 0
    for i in tasks:
      n = n + 1
      print(f"{n}. {i}")
      print()
    tasknum = int(input())
    tasknum = tasknum - 1
    todelete = tasks.index(tasks[tasknum])
    print(f"""
    I will delete the following task:
    
    {tasks[tasknum]}

    Press 'y' to confirm or any other letter to cancel...
    """)
    confirmtaskdelete = input()
    if confirmtaskdelete == "y" or confirmtaskdelete == "Y":
      tasks.remove(tasks[todelete])
      print()
      print("Task removed!")
      print()
    else:
      print("Fiu! That was close! No task was deleted.")
    time.sleep(1)
    os.system("clear")

  # Edit task
  elif action == "4":
    print()
    print("Edit task")
    print()
    print(f"{c('white')}Which task you want to edit? Press the number")
    print()
    for i in range(len(tasks)):
      print(f"{i+1}. {tasks[i]}\n")
    print()
    editTask = int(input())
    for i in range(len(tasks[counter])):
      if editTask <= len(tasks):
        print()
        print(f"""The task you are going to replace is:
        
        {i+1}. {tasks[editTask-1]}
        
        Press 'y' to proceed.
        
        """)
        editConfirm = input()
        if editConfirm == "y" or editConfirm == "Y":
          print()
          print("Write the new task:\n")
          print()
          addEditTask = input()
          tasks[editTask-1]=addEditTask
          print()
          print("Task replaced!")
          print()
        else:
          print("That was close! No task was replaced.")
          continue
      else:
        print(f"You have {len(tasks)} tasks, less than the number you wrote ({editTask})")

    # Nuke list

  elif action == "5":
    danger = "⚠️  💣  ⚠️  💣  ⚠️"
    print()
    print(f"{danger:^35}")
    print()
    print("THIS OPTION WILL ERASE THE WHOLE TO DO LIST CONTENT ")
    print()
    print(f"{danger:^35}")
    print("Press 'y' to confirm you want to do this...")
    print()
    deleteConfirm = input()
    if deleteConfirm == 'y' or deleteConfirm == 'Y':
      print()
      print("This action is undoable. Just to be sure... Press 'y' again.")
      deleteConfirm = input()
      if deleteConfirm == 'y' or deleteConfirm == 'Y':
        tasks = []
        print()
        print("All of your tasks have been deleted!🤯")
        print()
    continue