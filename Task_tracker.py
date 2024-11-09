# Task tracker
#import sys
from Automation import *
document_name = 'my_tracker.txt'


name_of_task = input('Give a name to your task tracker: ')
print("Enter 'end' to quit")
task_name(document_name, name_of_task)
while True:
    Tasks = input("My tasks for the day: ").lower()
    if Tasks == 'end':
        break

    add_text(document_name, Tasks)

display_file(document_name)
check_list(document_name)

