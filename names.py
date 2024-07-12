name = input("What's your name? ")

file = open("names.txt", "w") #"w" recreates the file everytime 

file.write(name)
file.close()

