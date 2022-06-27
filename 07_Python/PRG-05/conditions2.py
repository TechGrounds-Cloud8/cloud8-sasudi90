x = 0

#keep running function until x = 100 else break out of function
while x != 100: 
    try:
        x = int(input("Please input a number: "))
    
        if x > 100:
            print("Wow,", x, "is a big number!")
        elif x < 100:
            print(x, "is a pretty low number")
        else:
            print(x, "is a nice number indeed.")
            break
    except:
        #if input isn't an integer
        print("No number m8 :(")