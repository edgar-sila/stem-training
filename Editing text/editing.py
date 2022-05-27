#opening and editing files in python
role_file=open("roles.txt","r")
print(role_file.readline())
#close file.
role_file.close()

#read
file =open("roles.txt","r")
words=file.read()
print(words)

file=open("roles.txt","a")
file.write("i love python")
file.close()

file=open("./roles.txt","a")
file.write("i also love gaming")
file.close()

