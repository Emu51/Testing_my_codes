phonebook={}

def display_contact():
    ### print("Name\t\tContact Number\t\tAddress\t\tEmail")
    for key in phonebook:
        print(key)
        for x in phonebook:
        #print("{}\t\t{}".format(key,phonebook.get(key)))
              print(phonebook)
        




while True:
    choice= int(input(" 1. Add Contact \n 2.Update Contact \n 3.Delete Contact \n 4.Display Contact \n 5.Search Conatct \n 6.Quit \n Enter your Choice"))
    if choice == 1:
        name = input ("Enter the contact name ")
        phone = input(" Enter the mobile number ")
        address = input(" Enter Your Address ")
        email = input("Enter Your Email ")
        li=[phone,address,email]
        phonebook[name]= li
        #phonebook[name]= address
        #phonebook[name]= email


    elif choice == 2:
        update_contact = input("Enter the upadte contact ")
        if update_contact in phonebook:
            phone = input("enter mobile number ")
            address = input("enter adress ")
            email = input("enter email ")
            phonebook[update_contact]= li
            #phonebook[update_contact]= address
            #phonebook[update_contact]= email
            
            print("contact updated")
            display_contact()
        else:
            print("contact not found")

    elif choice == 3:
        del_contact = input("Enter the delete contact ")
        if del_contact in phonebook:
            confirm = input("Do you want to delete this number y/n? ")
            if confirm =='y' or confirm == 'Y':
                phonebook.pop(del_contact)
            display_contact()

        else:
            print("Name is not found in phonebook")


    elif choice == 4:
        if not phonebook:
            print("empty phonebook")
        else:
            display_contact()
    
        

    elif choice == 5:
        search_name =  input("Enter the contact name ")
        if search_name in phonebook:
            print(search_name,"Contact number is ",phonebook[search_name])
        else:
            print("contact number is not found")
    
    else:
        break
    

        
            
        
