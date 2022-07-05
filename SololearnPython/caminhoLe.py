import os
# The directory that 'test.py' is stored
directory = os.path.dirname(os.path.abspath(__file__))
# The path to the 'checklist.txt'
checklist_path = os.path.join(directory, 'countryList.txt')

file = open("/home/danieldfb/Daniel/Python/SololearnPython/countryList.txt","r")
cont = file.read()
str = len(cont)
print(cont)
print (str)

file = open("/home/danieldfb/Daniel/Python/SololearnPython/countryList.txt","r")
print (file.readlines())

file = open("/home/danieldfb/Daniel/Python/SololearnPython/countryList.txt","r")
for line in file:
    print(line)
file.close()


file.close()