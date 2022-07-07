names = ["John", "Oscar", "Jacob"]

file = open("names.txt", "w+")
#write down the names into the file
for i in range(len(names)):
    file.write(names[i])

file.close()

file= open("names.txt", "r")
#output the content of file in console
for i in range(len(names)):
    print(names[i])

file.close()

"""
Complete the program to create a file where you write the names from the list, each on a new line, 
and separately output them.

Output
John
Oscar
Jacob
Remember that "\n" represents a new line.
"""