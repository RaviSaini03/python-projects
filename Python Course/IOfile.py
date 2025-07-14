# f = open('intro.txt', 'w')

# f.write("My Name is Ravi Saini")

# with open('intro.txt', 'a') as f:
#     f.write("\nI live in Sikar, Radhakishanpura.")

#READLINE() METHOD

# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line)

# i = 0
# while True:
#     i = i+1
#     line = f.readline()
#     if not line:
#         break
#     m1 = int(line.split(',')[0])
#     m2 = int(line.split(',')[1])
#     m3= int(line.split(',')[2])
#     print(f"Marks of Roll no. {i} in Maths is: {m1}")
#     print(f"Marks of Roll no. {i} in Chemsitry is: {m2}")
#     print(f"Marks of Roll no. {i} in Physics is: {m3}")

#WRITELINE() METHOD

# lines = ['Roll no. 1\n','Roll no. 2\n','Roll no. 3']
# f.writelines(lines)
# f.close()

#SEEK() and TELL()

# with open('intro.txt','r') as f:

#     f.seek(10)
#     print(f.tell())
#     intro = f.read(5)
#     print(intro)

#TRUNCATE()

with open('intro.txt', 'w') as f:
    f.write("Ravi Saini")
    f.truncate(6)

with open('intro.txt', 'r') as f :
    print(f.read())