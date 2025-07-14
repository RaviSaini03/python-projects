#without map method

# def cube(x):
#     return x*x*x

# l = [1,2,3,4,5]

# newl = []
# for i in l:
#     newl.append(cube(i))

# print(l)
# print(newl)

#with map method or lambda method

# l = [1,2,3,4,5]

# newl = list(map(lambda x: x*x*x, l))
# print(l)
# print(newl)

#without filter function

# l = [1,2,3,4,5,6]

# newl = []
# for i in l:
#     if(i>3):
#         newl.append(i)
# print(newl)

#with filter Function

# l = [1,4,39,57,37,83,58]

# newl = list(filter(lambda x: x>5, l))
# print(l)
# print(newl)

#with reduce method
from functools import reduce

l = [1,2,3,4,5]

def totalSum(x,y):
    return x + y

sumOfList = reduce(totalSum, l)
print(sumOfList)

