file = open("myfile.txt", "w")
file.write("hello Students")
file.close()

file = open("myfile.txt", "a")
file.write("\nWelcome to Python")
file.close()

file = open("myfile.txt", "r")
data = file.read()
print(data)
file.close()