name = input("What's your name? ")

file = open("names.txt", "a") #"w" recreates the file everytime "a" will append to the bottom of the file

file.write(name)
file.close()

