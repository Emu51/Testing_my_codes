import json
filename = "todo.json"
todolist = {}
def addevent():
    date = input("Enter a Date in DD/MM/YYYY format\n")
    desc=input("Enter a description\n")
    time=input("Enter a time\n")
    place=input("Enter place name\n")
    if date in todolist:
        if time in todolist:
            print("An event at that time already exists \n Please select a different time")
            time2=input("Enter a different time")
            todolist[date] = desc,time2,place
        else:
            todolist[date] = desc,time,place
def search():
    search_date=input("Search a date (DD/MM/YYYY) \n ")
    if search_date in todolist:
        print(todolist[search_date])
    else:
        print("No event found on that date\n")
def display():
    print(todolist)
def edit():
    edit_list = input("enter a date (DD/MM/YYYY)\n")
    if edit_list in todolist:
        desc=input("Enter a description\n")
        time=input("Enter a time\n")
        place=input("Enter place name\n") 
        todolist[edit_list]=desc,time,place
        print("List Updated !")
    else:
        print("The date is not in the todo list")
def delete():
    rem = input("Enter the event date to be deleted")
    if rem in todolist:
        confirm = input("Confirm deleting this todolist? y/n")
        if confirm=='y'or confirm == 'Y':
            todolist.pop(rem)
        display()
    else:
        print("Event Not deleted !")
def store():
    with open(filename , 'a') as f:
        json.dump(todolist,f)