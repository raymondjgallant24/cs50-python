name = input("What's your name: ").capitalize()
match name :
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _ :
        print("Who?")