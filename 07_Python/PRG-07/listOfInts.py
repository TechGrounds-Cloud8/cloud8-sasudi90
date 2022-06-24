myList = [9, 80, 16, 67, 35]
x = 0
# len() = aantal objecten in array list
z = (len(myList))

for x in range(z):
    if x == z - 1:
        #print("Number stored in myList[",x,"] plus number stored in myList[ 0 ]")
        #z= 5, maar array begint vanaf 0, dus z-1 geeft het laatste object aan in array
        print(myList[z-1] + myList[0])
    else: 
        #print("Number stored in myList[",x,"] plus number stored in myList[", x+1,"]")
        print(myList[x] + myList[x+1])
        x =+ 1