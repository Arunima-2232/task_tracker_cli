import argparse
import json
import os

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
    parser.add_argument("operation",choices=["add","delete","show"],help="Operation to perform")
    parser.add_argument("task",type=str,nargs="*",help="task to be added or deleted")
    args=parser.parse_args()
    data=load_data()

    next_id=max(map(int, data.keys()),default=0)+1

    try:
        task=" ".join(args.task)
        if args.operation=="add":
            data[str(next_id)]=task
            print(f"{task} added to task-list! ID: {next_id}")
        elif args.operation=="delete":
            task_id=None
            for key,value in data.items():
                if key==task:
                    task_id=key
                    break
            if task_id:
                print(f"{data[task_id]} deleted from task-list!")
                del data[task_id]
            else:
                print("Task doesn't exist")
        elif args.operation=="show":
            if not data:
                print("No tasks")
            else:
                print("To-Do")
                for key,value in data.items():
                    print(key+".",value)
        save_data(data)
                
    except ValueError as e:
        print(f"Error: {e}")

if __name__=="__main__":
    main()