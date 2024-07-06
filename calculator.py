import sys
def main():
    x = int(input("What's x? "))
    #x = int(sys.argv[1])
    print("x squared is ", square(x))
def square(n):
    return n * n 
    
if __name__ == "__main__":
    main()