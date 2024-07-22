with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",") #split returns a list
        print(f"{name} is in {house}")