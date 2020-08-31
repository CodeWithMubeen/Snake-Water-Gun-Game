import random
dic = {1: "Snake", 2: "Water", 3: "Gun"}
user = 0
cpu = 0
print("Welcome to Snake , Water , Gun Game\nYou have only 10 Attempts")
for i in range(1, 10+1):
    print(f"\nAttempts : {i}\n")
    rand = random.choice(list(dic.values()))
    while True:
        for key, value in dic.items():
            print(f"Select {key} for {value}")
        select = 0
        try:
            select = int(input("\n"))
            if select > 3:
                print(" PLEASE INPUT 1,2,3 NUMBERS ".center(100, "*"))
            else:
                break
        except:
            print(" ONLY NUMBERS ALLOW ".center(100, "*"))
    print(f"\t\t\tYou selected [{dic[select]}] and computer selected [{rand}]")
    if dic[select] == rand:
        print("\n\t\t\tTie")
        user += 50
        cpu += 50
        print(
            f"\n\t\t\tYour's Points : {user}\n\t\t\tComputer Points : {cpu}\n")
    elif (dic[select] == "Snake" and rand == "Water") or (dic[select] == "Gun" and rand == "Snake") or (dic[select] == "Water" and rand == "Gun"):
        user += 100
        print(
            f"\n\t\t\tYour's Points : {user}\n\t\t\tComputer Points : {cpu}\n")
    else:
        cpu += 100
        print(
            f"\n\t\t\tYour's Points : {user}\n\t\t\tComputer Points : {cpu}\n")
print(
    f"\n\n\t\t\tTotal Your's Points : {user}\n\t\t\tTotal Computer Points : {cpu}")
if user > cpu:
    print("\n\t\t\tYou Won")
elif user == cpu:
    print("\n\t\t\tGame are Tie")
else:
    print("\n\t\t\tYou Lose")
