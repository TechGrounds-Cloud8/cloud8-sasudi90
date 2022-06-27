#declare  x en y 
x = int(input('First number: '))
y = int(input('Second number: '))

#function to have average of 2 input numbers
def avg(x, y):
    z = (x + y) / 2
    #for a function to return a value it must RETURN 
    return z

print('Average of numbers: ', avg(x, y))