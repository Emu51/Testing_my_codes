import jackfruit


while True:
    choice = int(input(" 1.Add new contact \n 2.Search Contact \n 3.Display Contacts \n 4.Edit Contact \n 5.Delete Contact \n 6.store contacts in a file "))
    if choice==1:
        jackfruit.addkey()
    elif choice==2:
        jackfruit.search()
    elif choice ==3:
        jackfruit.display()
    elif choice == 4:
        jackfruit.edit()
    elif choice == 5:
        jackfruit.delete()
    elif choice == 6:
        jackfruit.store()
    else:
        break