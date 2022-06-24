y = 0
hundred = True 

while hundred:
    x = input("Please input a number: ")
    y = int(x)
    
    if y == 100:
        print(y, "is a nice number indeed.")
        hundred = False
        break
    elif y < 100:
        print(y, "is a pretty low number")
    else:
        print("Wow,", y, "is a big number!")