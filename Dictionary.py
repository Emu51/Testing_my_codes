filename = "dic.txt"
file = open(filename, "a+")
file.close


def main_menu():
    choice= int(input("      Dictionary   \n 1. Add Keyword \n 2.Update Keyword \n 3.Delete Keyword \n 4.Display Keyword \n 5.Search Keyword \n 6.Quit \n Enter your Choice"))
    if choice == 1:
        Add()

    elif choice == 2:
        Update()  

    elif choice == 3:
        Delete()
       

    elif choice == 4:
        file = open(filename, "r+")
        file_content = file.read()
        if len(file_content) == 0:
            print("There is no keyword")
        else:
            print(file_content)
        file.close
                
    elif choice == 5:
        SearchUser()

    elif choice == 6:
        exit()
    else:
        print("Wrong Input \n")
    main_menu()

def Add():
    key = input('Enter the Keyword name ')
    desc = input('Description ')
    code = input('Code for the Keyword')
    keyword = ("" + key + "," + desc + "," + code + "\n")

    file = open(filename, "a")
    file.write(keyword)
    print("Add Keyword")


def Update():
    update_name = input("Enter the Keyword name ")
    file = open(filename, "r+")
    file_contents = file.readlines()
    item = False

    for line in file_contents:
        if update_name in line:
            key = input('Enter the Keyword name ')
            desc = input('Description ')
            code = input('Code for the Keyword')
            keyword = ("" + key + "," + desc + "," + code + "\n")

            file = open(filename, "a")
            file.write(keyword)
            print("Keyword Updates")
            item = True
            break
    if item == False:
        print("not found " + update_name)


def SearchUser():
    search_name = input("Enter the Keyword name ")
    file = open(filename, "r+")
    file_contents = file.readlines()
    item = False
    for line in file_contents:
        if search_name in line:
            print(line)
            item = True
            break
    if item == False:
        print("not found" + search_name)


def Delete():
    delete_name = input("Enter keyword name ")
    file = open(filename, "r+")
    file_contents = file.readlines()
    item = False
    for line in file_contents:
        if delete_name in line:
            del delete_name
            print("Deleted")

            item = True
            break
    if item == False:
        print("not found " + delete_name)


main_menu()
    
