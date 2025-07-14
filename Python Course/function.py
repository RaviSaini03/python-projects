def sumCal(a,b):
    sum = a+b
    print(sum)
def compare(a,b):
    if(a>b):
        print("a is greater")
    else:
        print("b is greater or both are equal")

a = int(input("enter value of a:"))
b = int(input("enter value of b:"))

sumCal(a,b)
compare(a,b)