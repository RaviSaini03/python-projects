# def myIntro(mname = "Ravi", lname = "Saini"):
#     print("my name is", mname, lname, ".")

# myIntro()
# myIntro("Albert", "Eienstine")

def average(*number):
    sum = 0
    for i in number:
        sum = sum + i
    print("the average of numbers is: ", sum/len(number))

average(1,5,6)