# we can use lambda function insteed of making small functionality functions in python

def inFunction(fx, int):
    sum = int + fx(int)
    return sum

square = lambda x: x*x
cube = lambda x: x*x*x
avg = lambda x,y,z: (x+y+z)/3

print(square(5))
print(cube(8))
print(avg(3,5,10))
print(inFunction(lambda x: x*5, 4))