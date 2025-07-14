import time

t = time.localtime()
current_time = time.strftime("%H:%M:%S")
# print(current_time)
current_hour = int(time.strftime("%H"))
# print(current_hour)
current_min = int(time.strftime("%M"))
# print(current_min)
current_sec = int(time.strftime("%S"))
# print(current_sec)


if current_hour > 00 and current_hour < 12 :
    print("Good Morning Sir!!")
elif current_hour > 12 and current_hour < 4 :
    print("Good Afternoon Sir!!")
else :
    print("Good Night Sir!!")