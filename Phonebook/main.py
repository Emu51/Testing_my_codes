#it is a console based phonebook application Build 1.00
import apple


while True:
    choice = int(input(" 1.Add new contact \n 2.Search Contact \n 3.Display Contacts \n 4.Edit Contact \n 5.Delete Contact \n 6.store contacts in a file "))
    if choice==1:
        apple.addname()
    elif choice==2:
        apple.search()
    elif choice ==3:
        apple.display()
    elif choice == 4:
        apple.edit()
    elif choice == 5:
        apple.delete()
    elif choice == 6:
        apple.store()
    else:
        break