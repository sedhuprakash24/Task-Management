from pymongo import MongoClient
URI = "mongodb://localhost:27017"
connection = MongoClient(URI)
Database = connection.Task_Management
collection = Database.Tasks

def menu():
    print("""
1. Add Task
2. View Task
3. Mark Task as Completed
4. Delete Task
5. Exit""")
        
def add_task():
    task_name=input("Enter the Task Name : ")
    date = input("Enter the Date : ")
    collection.insert_one({"Name":task_name,"Date":date,"completed":False})
    print("Task Added")    

def view_tasks():
    view = collection.find()
    for i in view:
        print(i)

def mark_as_completed():
    view_tasks()
    task_num=int(input("Enter the Task Number : "))
    tasks= list(collection.find())
    task = tasks[task_num-1]
    collection.update_one({"_id":task["_id"]},{"$set":{"completed":True}})
    print("Marked as Completed")

def delete_task():
    view_tasks()
    task_num=int(input("Enter the Task Number : "))   
    tasks = list(collection.find())
    task = tasks[task_num-1]
    collection.delete_one({"_id":task["_id"]}) 
    print("Task Deleted Successfully")

def main():
    while True:
        menu()
        select = int(input("Enter Your Choice : "))
        if select==1:
            add_task()
        elif select==2:
            view_tasks()
        elif select==3:
            mark_as_completed()
        elif select==4:
            delete_task()
        elif select==5:
            print("Exiting the program....,Sayonara !")  
            break  
        else:
            print("Invalid Input....Baka !")  

main()