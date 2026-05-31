import requests
from datetime import timedelta,datetime
import json

class UserInterface:
##### THIS CLASS IS TO FOCUS ON THE CLI-BASED UI
#####

    def __init__(self):
        self.app=TaskList()

    def menu(self):
        options = {
                1: "Add Task",
                2: "Edit Task",
                3: "Remove Task",
                4: "List All Tasks",
                5: "Run Function",
                6: "Load File",
                7: "Add an Entry",
                8: "Delete an Entry",
                0: "Close"
                }
        print()
        print("TODO App\n")
        for item,menu_item in options.items():
            print(f"{item}: {menu_item}")
        print()

    def start(self):
        print()
        while True:
            self.menu()
            entry= input("Entry:")
            print()
            print("TASK MENU")
            print("TASKLIST MENU")
            print()

            if entry == "0":
                self.app.close()
                break
            elif entry == "1":
                print("-- Add a task --")
                print()
                details={}
                details['Name']= input("Name of Task: ")
                details['Group']=input(f"Group for '{details['Name']}'': ")
                details['Frequency']=input("Frequency: ").upper() 
                details['id']= 0

                if details['Frequency']=="C":
                    details['interval'] = int(input("Enter Custom interval:"))
                self.app.add_task(Task(details))
                print()                
            elif entry == "2":
                print("\n-- Edit a Task --\n")
                print(f"{"-"*73}")
                print(f"||{"Entry":^3}||{"Name":^30}|{"Group":^10}|{"Frequency":^11}|{"Interval":^10}|")
                print(f"{"-"*73}")

                self.app.edit_task()
            elif entry == "3":
                self.remove_task()
            elif entry == "4":
                self.app.list_all()
            elif entry == "5":
                self.app.run_function()
                
            elif entry == "6":
                file_input=input("(M)ain or any for (T)esting file: ")
                self.app.load_file(file_input)
            elif entry == "7":
                self.add_entry()
            elif entry == "8":
                self.edit_entry()


    def remove_task(self):
        print("\n-- Remove a task --\n")
        for task in self.app.tasklist.values():
            print(f"{task.id}: {task.name}")
        choice=int(input(f"\nPick a number (< {len(self.app.tasklist)}): "))
        self.app.remove_task(choice)        
        print()

    def add_entry(self):
        print("\n-- Add an Entry --\n")
        for task in self.app.tasklist:
            print(f"{task.id}: {task.name}")
        choice=(int(input(f"\nPick a number (< {len(self.app.tasklist)}): "))-1)
        entry=input("(T)oday or Different Date,[DDMMYY]: ")
        self.app.tasklist[choice].add_entry(entry)        
        print()

    def edit_task(self):
        pass

class Task:
##### class Task, is a child of the Tasklist. This holds the specifics of the task. 
# will be task-specific activities, provide it with task attributes and methods of operation on a task from the tasklist dict.

##### Methods:
###          edit_task
###          add_entry
###          task_stats
###          set_interval

### attributes: name, id, group, frequency, interval, completions, added
    def __init__(self,deets):
        if 'Name' in deets:
            self.name=deets['Name']
        # except TypeError:
        #         self.name=deets['']
        else:
            self.name="No Name"
        if 'completions' in deets:
            date_list=[]
            if len(deets['completions'])==0:
                self.completions=date_list
            else:
                for item in deets['completions']:
                    item=datetime.strptime(item,'%d%m%y')
                    date_list.append(item)
                    self.completions=date_list
        else:
            self.completions=[]
        self.group=deets['Group']
        self.freq=deets['Frequency']
        if self.freq == "C":
            self.interval=deets['interval']
        else:
            self.interval=self.set_interval()
        
        self.added=datetime.today()
        self.id=deets['id']


    def set_interval(self):
        intervals={"D":1,
                    "W": 7,
                    "BW": 14,
                    "F": 15,
                    "M": 30,
                    "Q": 90,
                    "Y": 365,
                    "I": 0
                    }

        if self.freq in intervals:
            return intervals[self.freq]
        else:
            return 0


    def add_entry(self,entry):
        entry=entry.upper()
        if entry == "T":
            processed=datetime.today()
        else:
            processed=datetime.strptime(entry,'%d%m%y')

        self.completions.append(processed)
        
    
    def edit_task(self,entry,name):
        if entry == "N":
            self.name=name
        elif entry == "F":
            self.freq=name
            self.set_interval()
        elif entry == "G":
            self.group=name
        

    def task_stats():
        pass

class TaskList:
##### class TaskList, will be taskList-specific activities, ie: actions that will be taken against the whole tasklist.
##### provide it with task attributes and methods of operation on a task from the tasklist dict.

##### Methods:
###          add_task,
###          remove task,
###          run_function,
###          load_file, 
###          close(), 
###          list_all

    def __init__(self):
        self.tasklist=[]
        self.id=0

### ADD A TASK TO TASKLIST
    def add_task(self,dts:Task):
        self.id+=1
        dts.id=self.id
        self.tasklist.append(dts)
    
    def set_interval(self,entry):
        intervals={"D":1,
                    "W": 7,
                    "BW": 14,
                    "F": 15,
                    "M": 30,
                    "Q": 90,
                    "Y": 365,
                    "I": 0
                    } 

        if entry in intervals:
            return intervals[entry]
        else:
            return intervals['I']

    def edit_task(self):
        while True:
            entry=0
            for task in self.tasklist:
                entry+=1
                print(f"||{entry:^5}||{task.name:^30}|{task.group:^10}|{task.freq:^11}|{task.interval:^10}|")
            choice=(int(input("\nPick an entry:"))-1)
            if choice > len(self.tasklist):
                print("Enter a lower entry")
            else:
                print(f"Details of task:\nName: {self.tasklist[choice].name}\nFrequency: {self.tasklist[choice].freq}\nInterval: {self.tasklist[choice].interval} days\nGroup: {self.tasklist[choice].group}")
                taskedit=input("Enter 'N' to update Name, 'F' for Frequency, 'G' for Group:").upper()
                if taskedit == "N":
                    self.tasklist[choice].name=input("Enter new Task name: ")
                elif taskedit == "F":
                    self.tasklist[choice].freq=input("Enter new Task frequency: ").upper()
                    if self.tasklist[choice].freq == "C":
                        self.tasklist[choice].interval = int(input("Set interval: "))
                    else:
                        self.tasklist[choice].interval=self.set_interval(self.tasklist[choice].freq)
                    
                elif taskedit == "G":
                    self.tasklist[choice].group=input("Enter new Task group: ")

                break

### REMOVE A TASK FROM TASKLIST
    def remove_task(self,input):
        print(f"Removing {input}: {str(self.tasklist[input].name)}")

        del self.tasklist[input]
                
### RECURSIVELY RUN TASKLIST TO FIND ITEMS DUE:
    def run_function(self):
        filename="main_todo.json"

### LOAD A set of TASKs TO TASKLIST
    def load_file(self,input):
        self.filename="main_todo.json"
        if input != "M":
            self.filename="todo.json"
        self.fileloader=FileLoader()
    
        tasklist_temp=self.fileloader.load_file(self.filename)
        
        for details in tasklist_temp.values():
            self.id+=1
            details['id']=self.id
            self.tasklist.append(Task(details))
        
    
### LOAD A set of TASKs TO TASKLIST

    def close(self):
        ct={}
        for values in self.tasklist:

            info={}
            info['Name']=values.name
            info['Added On']=datetime.strftime(values.added,'%d%m%y')
            info['Frequency']=values.freq
            try:
                info['interval']=values.interval
            except AttributeError:
                info["interval"]=0
            info['Group']=values.group
            comps=[]
            for i in values.completions:
                comps.append(datetime.strftime(i,'%d%m%y'))
            info['completions']=comps
            ct[values.id]=info
        print('Closed')
        self.fileloader.close(ct)


    def list_all(self):
        testList=[]
        if len(self.tasklist) > 0:
            print("\nTasks in current tasklist:\n")
            print(f"||{"Task ID":^10}|| {"Name":^20}|{"# of Entries":^15}|{"Last Completed":^16}|")
            for task in self.tasklist:
                testList.append((task.id,task.name))
                
                if len(task.completions)==0:
                    comps=0
                    le=0
                else:
                    comps=len(task.completions)
                    le=datetime.strftime(task.completions[-1],'%d.%m')
                print(f"||{task.id:^10}|| {task.name:^20}|{comps:^15}|{le:^16}|")
                
            print()
        else:
            print("\nNo Tasks loaded. Add One or Load a File\n")


### Function to run on CLI that displays tasks overdue.

    def run_function(self):
        due=self.run_item()
        print("*"* 72)
        for item in due:
            totlen=len(item[0]) + len(str(item[1]))+ len(item[2])
            div=72-totlen
            if div // 2 != 1:
                div+=1
            if item != None:
                print(f"*{(" "*int(div/2))}{item[0]}, due {item[1]} days ago. Last completed: {item[2]}{(" "*int(div/2))}  *")

    def run_item(self):
        due=[]
        for task in self.tasklist:
            if task.freq == "I":
                pass
            else:
                try:  
                    task.completions.sort()
                    lastDate=task.completions[-1]
                    interval=timedelta(days=task.interval)
                    nextDate=lastDate+interval
                    today=datetime.today()
                    duration=today-nextDate
                    if nextDate < today:               
                        due.append(self.format_data((task.name,duration,lastDate)))
                except IndexError:
                    pass
        return due

### Function to send info to ntfy.olav.pw
    def run_function2(self):
        due=self.run_item()
        data=""
        for item in due:
            data+=(item[0]+"\n")
        # print(data)
        requests.post("https://ntfy.olav.pw/todos",
            data=data,
            headers={ "Title": "Todo's Daily Update" })

### Create function that takes tasks due, and provides a string format variable.                
    def format_data(self,taskdue:tuple):
        name=taskdue[0]
        daysOverdue=taskdue[1].days
        lastDay=int(datetime.strftime(taskdue[2],'%d'))
        lastWD=datetime.strftime(taskdue[2], '%A')
        lastMT=datetime.strftime(taskdue[2], '%b')        
        nums={1:"st",
              2:"nd",
              3:"rd"
              }

        if lastDay in nums:
            add=nums[lastDay]
            lastDay=str(lastDay)+add
        else:
            lastDay=str(lastDay)+"th"
        date=f"{lastWD}, {lastDay} {lastMT}"
        return name,daysOverdue,date

class FileLoader:
##### class FileLoader, will focus on opening and closing the main/testing json or a future database reader.

##### Methods: 
###          load_file- READ information from filename provided and return a dictonary.
###          close- WRITE a json and dump the dictionary provided.

    def __init__(self):
        self.filename=""

    def load_file(self,file):
        self.filename=file
        with open (self.filename,"r") as doc:
            temp_tasklist= json.load(doc)
            return temp_tasklist

    def close(self,close):
        with open(self.filename, "w") as doc:
            json.dump(close, doc)
        
        
        
