import json
filename = "keys.json"
keys = {}
def addkey():
    key = input("Enter a key")
    desc=input("Enter discription")
    code=input("Enter code snippet")
    
    keys[keys] = desc,code
def search():
    search_key=input("Search a keys:")
    if search_key in keys:
        print(keys[search_key])
    else:
        print("Name not found")
def display():
    print(keys)
def edit():
    edit_keys = input("enter keys keys")
    if edit_keys in keys:
        desc = input("Enter new description")
        code = input("Enter new code")
         
        keys[edit_keys]=desc,code
        print("keys Updated !")
    else:
        print("The key is not in the keys list")
def delete():
    rem = input("Enter the keys keys to be deleted")
    if rem in keys:
        confirm = input("Confirm deleting this keys? y/n")
        if confirm=='y'or confirm == 'Y':
            keys.pop(rem)
        display()
    else:
        print("keys No deleted !")
def store():
    with open(filename , 'a') as f:
        json.dump(keys,f)