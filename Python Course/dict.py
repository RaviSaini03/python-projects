dict = {
    "Ravi": 90,
    "Pawan": 40,
    "Sandeep": 60,
    "Piyush": 85,
    "Priyanshu": 00
}
# print(dict)
# print(dict["Ravi"])
# print(dict['Karan']) # if element is not exit in dict then this will give error
# print(dict.get('Karan')) # "     "    '   ''' ''''''''''''''not throw errer, this will throw none
for i in dict.keys():
    print(f"Marks of {i} is {dict[i]}")