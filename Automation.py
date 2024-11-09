document_name = 'my-tracker.txt'
import sys


def add_text(document_name, tasks):
    with open(document_name, 'a') as tracker:
            record_keeper = tracker.write(tasks)


#task_name = 'my_tracker.txt'
def  task_name(document_name,name_of_task):
      with open(document_name, 'w') as to_do:
            to_do_list = to_do.write(name_of_task) 


def display_file(document_name):
      with open(document_name) as contents:
            file_contents = contents.read()
            print(file_contents)


def check_list(document_name):
      check_off = str(input('Name of completed task: ')).lower()
      with open(document_name, 'r') as task_list:
            task_tracked = task_list.readlines()
            print(task_tracked)

      for tracked in task_tracked:
            if tracked.startswith(check_off):
                  successful = f'{tracked} ** Completed.'
                  print(successful)
      
      with open(document_name, 'a') as checked:
            cancel_off_list = checked.write(f'\n{successful}')