def readline():
    #reads lines in file and returns them
    filename='test2.txt'
    with open(filename, 'r') as f:
        content = f.readlines()
        return content

def addline(string):
    #adds a line at the end of the file
    filename='test2.txt'
    with open(filename, 'a') as f:
        f.write("\n")
        f.write(string)

