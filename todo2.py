##Todo app##

## Operation

## Create a tasklist ##
## Each task is added to the tasklist ##
## App can be UI facing or web-facing
## Will store entries into a database
## All functions must return variables that will be parsed by client-facing app. ie, Django, GUI

# Tasklist-Specific Ops
# Attributes:
# name:

# Add-        will add tasks into the main tasklist
# Edit-       edit a task in tasklist
# Delete-     delete, in tasklist
# Run-        run todo main function
# Load-       load entries into tasklist
# Close-      save all changes and exit

# Task-Specific Ops
# Each task has attributes- index, name, group, date added, frequency, interval
# Task attributes:
# index:    # of task in tasklist
# name      name of task
# added     date added
# frequency how often does the task repeat- D,W,BW,M,Y,I
# interval  numerical value of frequency

# group/category
# completed=[]

# Add/Edit/Delete an entry


from datetime import datetime

class Tasklist:
    def __init__(self):
        self.name="Olav's List"
        self.list=[]

    def add_task(self,details):
        details.append(len(self.list))
        self.list.append(Task(details))
        
    # def edit_task
    # def delete_task
    # def run
    # def load
    # def close

# index:    # of task in tasklist
# name      name of task
# added     date added
# frequency how often does the task repeat- D,W,BW,M,Y,I
# interval  numerical value of frequency

class Task:
    def __init__(self,details):
        self.name=details[0]
        self.freq=details[1]
        self.completed=[]
        self.added=datetime.today().strftime("%d/%m/%Y")
        self.index=details[3]+1
        self.interval=0
        self.group=details[2]

    # def add_entry
    # def edit_entry
    # def del_entry




a=Tasklist()
entry=0
while entry != 10:
    name="Task"+str( entry)
    freq=10-entry
    group="H"
    details=[name,freq,group]
    a.add_task(details)
    entry+=1


