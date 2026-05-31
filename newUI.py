class UserInterface:
    from datetime import date
    def __init__(self):
        pass

    def start(self):
        app=Tasklist()
        tl=FileLoader().load_file("main_todo.json")
        id=0
        for item in tl:
            id+=1
            app.add_task(tl[item],id)
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
        print("TO DO APP MENU\n")
        for key,value in options.items():
            print(f"{key}: {value}")
        print()
        
        while True:
            try:
                choice=int(input(f"Pick an option (less than {len(options)}): "))

                if choice == 1:
### Add a Task needs a dictonary that collects- name, group frequency, date Added, completions, id
                    task={}
                    frequency={"D":1,
                               "W": 7,
                               "BW": 14,
                               "F": 15,
                               "M": 30,
                               "Q": 90,
                               "Y": 365,
                               "I": 0}
                    task['name']=input("Enter a name: ")
                    task['group']=input("Enter a group: ")
                    freq=""
                    while freq not in frequency:
                        freq=input("Enter a frequency- (D,W,BW,F,M,Q,Y,I) ").upper()
                    if freq == "I":
                        interval=int(input("Enter custom interval: "))
                        task['interval']=interval
                        task['freq']=freq
                    else:
                        task['freq']=freq
                        task['interval']=frequency[freq]
                    
                    task['dateAdded']= self.date.today().isoformat()
                    task['completions']=[]
                    task['id']=0

                    app.add_task(task)
                    task={}

                elif choice == 4:
                    reply = app.list_tasks()
                    for item in reply:
                        print(item)
                elif choice == 3:
                    pass
                elif choice == 0:
                    break
            except (ValueError,KeyError):
                print("Invalid Entry")

class Tasklist:
    def __init__(self):
        self.tasklist=[]
        self.name="test"

    def add_task(self,info,id):
        entry=Task(info,id)
        self.tasklist.append(entry)

    def remove_task(self,info):
        pass

# Should return a object that is parseable, ie: dict,list

    def list_tasks(self):
            listOfTasks=[]
            if len(self.tasklist) > 0:
                listOfTasks.append("\nTasks in current tasklist:\n")
                listOfTasks.append(f"||{"Task ID":^10}|| {"Name":^20}|{"# of Entries":^15}|{"Last Completed":^16}|")
                for task in self.tasklist:
                    listOfTasks.append(f"||{task.id:^10}|| {task.name:^20}|{len(task.completions):^15}|")
            else:
                listOfTasks.append("No Tasks in List.")
            
            return listOfTasks

    def run_function():
        pass


class Task(Tasklist):
    def __init__(self,info,id):
        # super().__init__()
        try:
            self.name=info['name'] 
            self.id=info['id']
            self.dateAdded=info['dateAdded']
            self.completions=info['completions']
            self.freq=info['freq']
            self.interval=info['interval']
            self.group=info['group']
            self.id=id
        except (KeyError):
            self.name=info['Name']
            self.dateAdded=info['Added On']
            self.completions=info['completions']
            self.freq=info['Frequency']
            self.interval=info['interval']
            self.group=info['Group']
            self.id=id


        
class FileLoader:
    import json
##### class FileLoader, will focus on opening and closing the main/testing json or a future database reader.

##### Methods: 
###          load_file- READ information from filename provided and return a dictonary.
###          close- WRITE a json and dump the dictionary provided.

    def __init__(self):
        self.filename=""

    def load_file(self,file):
        self.filename=file
        with open (self.filename,"r") as doc:
            temp_tasklist= self.json.load(doc)
            return temp_tasklist

    def close(self,close):
        with open(self.filename, "w") as doc:
            self.json.dump(close, doc)


i=UserInterface()
i.start()