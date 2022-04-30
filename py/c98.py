f = open("test.txt","w+")
#print(f.read())
#print(f.readlines())
lines = ["My name is Shyaam\n", "I study in class 10\n","I am 16 years old"]
#f.write("I study in class 10")
f.writelines(lines)
print(f.writelines(lines))