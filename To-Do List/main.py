import orange


while True:
    choice = int(input(" 1.Add new Event \n 2.Search Date \n 3.Display To-do list \n 4.Edit Event \n 5.Delete Event \n 6.store To-do list in a file "))
    if choice==1:
        orange.addevent()
    elif choice==2:
        orange.search()
    elif choice ==3:
        orange.display()
    elif choice == 4:
        orange.edit()
    elif choice == 5:
        orange.delete()
    elif choice == 6:
        orange.store()
    else:
        break