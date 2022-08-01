import jackfruit


while True:
    choice = int(input(" 1.Add new Key \n 2.Search key \n 3.Display key \n 4.Edit key \n 5.Delete key \n 6.store all key in a file "))
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