import random

x = random.randint(1, 100)
N = int(input("Введи кол-во попыток: "))

print(f"!!!START!!! \nу тебя {N} попыток")

i = 1

while i <= N:
    term = int(input("Какое число загадано: "))
    if term == x:
        print("!!!WIN!!!")
        break
    if term < x:
        print("Больше")
    if term > x:
        print("Меньше")
    print("________________________________")
    i += 1
else:
    print("LOSE")
    print(f"загадано {x}")