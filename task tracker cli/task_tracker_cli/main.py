import argparse
import json
import os

from datetime import datetime

data_file = os.path.join(os.path.dirname(__file__), "data.json")

def load_data():
     if not os.path.exists(data_file):
          return {}
     with open(data_file,"r") as f:
          return json.load(f)

def save_data(data):
     with open(data_file,"w") as f:
          json.dump(data,f,indent=4)

def main():
    parser=argparse.ArgumentParser(description="A simple task tracking CLI application")
    parser.add_argument("operation",choices=["add","delete","update","mark-done","show","show-done","show-not-done"],help="Operation to perform")
    parser.add_argument("task",type=str,nargs="*",help="task to be added or deleted")
    args=parser.parse_args()
    data=load_data()

    next_id=max(map(int, data.keys()),default=0)+1

    try:
        task=" ".join(args.task)
        if args.operation=="add":
            data[str(next_id)]=[task,"Not done",datetime.now().strftime('%d/%m/%Y, %H:%M'),"--"]
            print(f"{task} added to task-list! ID: {next_id}")
        elif args.operation=="delete":
            task_id=None
            for key,value in data.items():
                if key==task:
                    task_id=key
                    break
            if task_id:
                print(f"{data[task_id][0]} deleted from task-list!")
                del data[task_id]
            else:
                print("Task doesn't exist")
        elif args.operation=="update":
            task_id=None
            for key,value in data.items():
                if key==args.task[0]:
                    task_id=key
                    data[task_id][0]=args.task[1]
                    data[task_id][3]=datetime.now().strftime('%d/%m/%Y, %H:%M')
                    break
            if task_id:
                print(f"Task {task_id} updated to {data[task_id][0]}!")
            else:
                print("Task doesn't exist")
        elif args.operation=="mark-done":
            task_id=None
            for key,value in data.items():
                if key==task:
                    task_id=task
                    data[task_id][1]="Done!"
                    data[task_id][3]=datetime.now().strftime('%d/%m/%Y, %H:%M')
                    break
            if task_id:
                print("Task marked as done!")
            else:
                print("Task doesn't exist")
        elif args.operation=="show":
            if not data:
                print("No tasks")
            else:
                print("To-Do")
                for key,value in data.items():
                    print(key+".",value[0],"-",value[1],"- created at",value[2],"- updated at", value[3])
        elif args.operation=="show-done":
            if not data:
                print("No tasks")
            else:
                task_id=None
                print("Tasks marked done:")
                for key,value in data.items():
                    if(value[1]=="Done!"):
                        task_id=key
                        print(key+".",value[0])
                if(task_id==None):
                    print("None")
        elif args.operation=="show-not-done":
            if not data:
                print("No tasks")
            else:
                task_id=None
                print("Tasks marked not done:")
                for key,value in data.items():
                    if(value[1]=="Not done"):
                        task_id=key
                        print(key+".",value[0])
                if(task_id==None):
                    print("None")
        save_data(data)
                
    except ValueError as e:
        print(f"Error: {e}")

if __name__=="__main__":
    main()
