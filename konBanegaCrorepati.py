# kon banega crorepati method 1

questions = [
    [
        '1. What is distance between Earth and Moon?', '(a) 1.8 Million km','(b) 2.5 Million km', '(c) 0.563 Million km','(d) 0.384 Million km', 4
    ],
    [
        "2. What is distance between Earth and Moon?", '(a) 1.8 Million km','(b) 2.5 Million km', '(c) 0.563 Million km','(d) 0.384 Million km', 4  
    ],
    [
        "3. What is distance between Earth and Moon?", '(a) 1.8 Million km','(b) 2.5 Million km', '(c) 0.563 Million km','(d) 0.384 Million km', 4  
    ],
    [
        "4. What is distance between Earth and Moon?", '(a) 1.8 Million km','(b) 2.5 Million km', '(c) 0.563 Million km','(d) 0.384 Million km', 4 
    ],
    [
        "5. What is distance between Earth and Moon?", '(a) 1.8 Million km','(b) 2.5 Million km', '(c) 0.563 Million km','(d) 0.384 Million km', 4  
    ],
    [
        "6. What is distance between Earth and Moon?", '(a) 1.8 Million km','(b) 2.5 Million km', '(c) 0.563 Million km','(d) 0.384 Million km', 4  
    ],
    [
        "7. What is distance between Earth and Moon?", '(a) 1.8 Million km','(b) 2.5 Million km', '(c) 0.563 Million km','(d) 0.384 Million km', 4  
    ],
]

levels = [1000, 2000, 5000, 10000, 30000, 50000, 100000]
money = 0
for i in range(0, len(questions)):
    question = questions[i]
    print(f"\n\nRs for the question is {levels[i]}")
    print(f"{question[0]}")
    print(f"{question[1]}        {question[2]}")
    print(f"{question[3]}        {question[4]}")
    reply = int(input("Give your answer: "))
    if(reply == question[5]):
        print(f"Your ans is correct, you won {levels[i]}")
        if(i == 2):
            money = 1000
        elif(i == 4):
            money = 30000
    else:
        print("Wrong ans")
        break

print(f"your total money is {money}")

# kon banega crorepati method 2

# science = ['1. What is distance between Earth and Moon?','2. What is speed of light?','3. In which galaxy our solar system is exist?', '4. Which is nearest galaxy to milky way galaxy', '5. What is scientific name of Cow?', '6. Which is the most avialable element on earth surface?','7. On which date Chandrayan 3 was landed on moon?']

# science1 = ('(a) 1.8 Million km','(b) 2.5 Million km', '(c) 0.563 Million km','(d) 0.384 Million km','(a) 30 Million m/s','(b) 3 Million m/s', '(c) 3 Billion m/s','(d) 300 Million m/s', '(a) Andromada', '(b) Milky Way', '(c) Whirlpool', '(d) Sombrero', '(a) Milky Way', '(b)Andromada', '(c) Whirlpool', '(d) Sombrero', '(a) Bos taurus', '(b)Loxodonta', '(c) Aves', '(d) Capra aegagrus hircus', '(a) zinc', '(b) carbon', '(c) Oxyzen', '(d) Silica', '(a) 23 August 2022', '(b) 13 August 2023', '(c) 20 August 2023', '(d) 23 August 2023',)


# def correctAns(index, ans):
#     ans = input("Write your option: ")
#     if(index == 0 and ans == "d"):
#         print("Your answer is correct.")        
#     elif(index == 1 and ans == "d"):
#         print("Your answer is correct.")       
#     elif(index == 2 and ans == "b"):
#         print("Your answer is correct.")
#     elif(index == 3 and ans == "b"):
#         print("Your answer is correct.")
#     elif(index == 4 and ans == "a"):
#         print("Your answer is correct.")
#     elif(index == 6 and ans == "d"):
#         print("Your answer is correct.")
    

# for index in range(len(science)):
#     if(index == 0):
#         print(science[index])
#         for i in range(4):
#             print(science1[i])
#         correctAns(index, 'ans')
#     elif(index == 1):
#         print(science[index])
#         for i in range(4,8):
#             print(science1[i])
#         correctAns(index, 'ans')
#     elif(index == 2):
#         print(science[index])
#         for i in range(8,12):
#             print(science1[i])
#         correctAns(index, 'ans')
#     elif(index == 3):
#         print(science[index])
#         for i in range(12,16):
#             print(science1[i])
#         correctAns(index, 'ans')
#     elif(index == 4):
#         print(science[index])
#         for i in range(16,20):
#             print(science1[i])
#         correctAns(index, 'ans')
#     elif(index == 5):
#         print(science[index])
#         for i in range(20,24):
#             print(science1[i])
#         correctAns(index, 'ans')
#     elif(index == 6):
#         print(science[index])
#         for i in range(24,28):
#             print(science1[i])
#         correctAns(index, 'ans')
#     else:
#         print("you lost")
#         break