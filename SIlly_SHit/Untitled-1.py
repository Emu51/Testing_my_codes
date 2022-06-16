import fun


new_line = input("Add a new line")
fun.addline(new_line)
output = fun.readline()
for line in output:
    print(line.rstrip())


 