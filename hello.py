def main():
    name = input("What's your name? ")
    print(hello(name))
    


def hello(name):
    return f"hello, {name}"

if __name__ == "__main__":
    main()