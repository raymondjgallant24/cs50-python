#Take user name as input 
name = input("What's your name? ").title().strip()

#SPLIT USERS NAME INTO FIRST NAME AND LASTNAME 
first, last = name.split()

#Greet the user using format string
print(f"Hello, {first}")



