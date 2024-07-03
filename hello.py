def main():
    name = input("What's your name? ").strip().capitalize()
    hello(name)
    return name


def hello(name):
    print(f"hello, {name}")

main()