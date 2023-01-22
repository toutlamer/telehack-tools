# ascii.py by omerien
# allows you to translate the whole ascii garbage satan.exe gives you 
# to a proper ascii string

import time

print("Enter/Paste your content. Leave an empty line to stop.")
contents = []
while True:
    line = input()
    if line == "":
        break
    line = line[5:]
    linearray = line.split(" ")
    contents.append(linearray)
starttime = time.time()

print("    01234567 89abcdef")
lineincrementer = 0
for i in contents:
    currline = ""
    charincrementer = 0
    for j in i:
        currchar = ""
        try:
            temp = int(j, 16)
        except:
            print("There was an error while treating a hex value. Make sure you inputted the dump right.")
            print("Hex value: " + j)
            exit()
        if temp < 32 or temp == 127:
            currchar = "."
        else:
            currchar = chr(temp)
        if charincrementer % 8 == 0:
            currline = currline + " " + currchar
        else:
            currline = currline + currchar
        charincrementer = charincrementer + 1
    linehex = hex(lineincrementer)
    if lineincrementer % 10 == 0 and lineincrementer != 0:
        print("    01234567 89abcdef\n\n    01234567 89abcdef")
    if len(linehex[2:]) == 1:
        linehex = "0" + linehex[2:]
    else:
        linehex = linehex[2:]
    print(linehex + " " + currline)
    lineincrementer = lineincrementer + 1
print("    01234567 89abcdef\n")
print(str(len(contents)) + " lines treated in " + str((time.time() - starttime)) + " seconds.")
