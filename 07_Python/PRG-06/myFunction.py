#create function and call it, second function is with unser input
def myFunction(): 
    print("Hello, world!")

name = input("Input string here: ") 

def mySecondFunction(name):
    print("Hello,", name,"!")

myFunction()
mySecondFunction(name)