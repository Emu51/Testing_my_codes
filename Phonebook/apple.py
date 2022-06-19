import json
filename = "contacts.json"
contact = {}
def addname():
    name = input("Enter a Contact Name")
    phone_number=input("Enter a Phone Number")
    address=input("Enter an address")
    email=input("Enter a Email")
    contact[name] = phone_number,address,email
def search(s):
    search_name=input("Search a name:")
    if search_name in contact:
        print(contact[search_name])
    else:
        print("Name not found")
def display():
    print(contact)
def edit():
    edit_contact = input("enter contact name")
    if edit_contact in contact:
        phone_number = input("Enter new phone number")
        address = input("Enter new address")
        email = input("Enter new email") 
        contact[edit_contact]=phone_number,address,email
        print("Contact Updated !")
    else:
        print("The name is not in the contact list")
def delete():
    rem = input("Enter the contact name to be deleted")
    if rem in contact:
        confirm = input("Confirm deleting this contact? y/n")
        if confirm=='y'or confirm == 'Y':
            contact.pop(rem)
        display()
    else:
        print("Contact No deleted !")
def store():
    with open(filename , 'a') as f:
        json.dump(contact,f)


