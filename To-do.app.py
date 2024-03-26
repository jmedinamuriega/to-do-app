import pprint
from datetime import datetime
now = datetime.now()
date = now.date()
print(date)
pp = pprint.PrettyPrinter(indent=4)
to_do_list={
    
}

while True:
    interface=input('''
    Welcome to the To-Do List App!

    Menu:
    1. Add a task
    2. View tasks
    3. Mark a task as complete
    4. Delete a task
    5. Quit
    ''')

        
    def add_task():
        if interface=="1":
            status="incomplete"
            task=input("Please introduce the task: ")
            to_do_list[task,date] = status
            add_more=input("Do you want to add something else(y)? ")
            if add_more=="y":
                add_task()                                      
                                  
    def complete_task():
        if interface == "3":
            task = input("Please put the name of the task that you completed: ")
            if (task, date) in to_do_list:
                to_do_list[(task, date)] = "completed"
                print("The task is now completed! Congrats!")
                add_more = input("Do you want to complete more tasks(y)? ")
                if add_more.lower() == "y":
                    complete_task()
    def delete_task():
        if interface == "4":
            task = input("What task do you want to delete? ")
            if (task, date) in to_do_list:
                to_do_list.pop((task, date))
                delete_more = input("Do you want to delete more tasks(y)? ")
                if delete_more.lower() == "y":
                    delete_task()
            else:
                print("The task does not exist.")          
            
    def view_task():
        if interface == "2":
            print("Here is the list of your tasks!")
            for (task, date), status in to_do_list.items():
                print(f"Task: {task}, Status: {status}, Date: {date}")   
    if interface=="1":
        add_task()
    elif interface=="2":
        view_task()
        leave=input("Do you want to do leave(y)? ")
        if leave=="Y":
            break
    elif interface=="3":
        complete_task()
    elif interface=="4":
        if len(to_do_list)==0:
            print("There is no tasks pendant!")
            break
        elif len(to_do_list)>0:
            delete_task()    
    elif interface=="5":
        print("I hope you are doing well!")
        break
              
    
        