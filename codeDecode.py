# encoding part
import string
import random
text = input("Enter any text: ")
x = text.split()
y = list()

def firstLetter(res1):
    res1 = ''.join(random.choices(string.ascii_uppercase + string.digits, k=3))
    res11 = str(res1)
    updated3 = res11 + updated2
    return updated3

def lastLetter(res2):
    res2 = ''.join(random.choices(string.ascii_uppercase + string.digits, k=3))
    res21 = str(res2)
    updated5 = updated4 + res21
    return updated5

def reverse(orignal1):
    str1 = ''
    for i in orignal1:
        str1 = i + str1
    return str1

def nextWord(orignal2):
    first_letter = orignal2[0]
    last_letter = orignal2[-1]
    middle_string = orignal2[1:-1]
    modified = last_letter + middle_string + first_letter
    return modified

for i in range(0, len(x)):
    length = len(x[i])
    if(length <= 2):
        orignal1 = x[i]
        updated1 = reverse(orignal1)
        y.append(updated1)
    elif(length >= 3):
        orignal2 = x[i]
        updated2 = nextWord(orignal2)
        updated4 = firstLetter(updated2)
        updated6 = lastLetter(updated4)
        y.append(updated6)
    else:
        print("envalid input")

code = ' '.join(y)
print(code)

# decode part
decodeWilling = input("\nDo you want to decode this: ")
z = list()

def sliceWord(duplicate2):
    modified = duplicate2[3:-3]
    return modified

if(decodeWilling == "yes"):
    decodeCode = code.split()

    for i in range(0, len(decodeCode)):
        length = len(decodeCode[i])
        if(length <= 2):
            duplicate1 = decodeCode[i]
            updated1 = reverse(duplicate1)
            z.append(updated1)
        elif(length >= 3):
            duplicate2 = decodeCode[i]
            decodedWord1 = sliceWord(duplicate2)
            decodedWord2 = nextWord(decodedWord1)
            z.append(decodedWord2)
        else:
            print("invalid Input")

decode = " ".join(z)
print(decode)

# add this
