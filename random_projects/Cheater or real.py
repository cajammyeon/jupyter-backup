import random

x = ["Head", "Tail"]
print("How many flips do you want ?")
flips = int(input())
character1 = random.randint(1, 2)

if character1 == 1 : #this is for cheater
    flip_result = random.choices(x, weights=(1, 3), k=flips)
    print("Head : " + str(flip_result.count("Head")))
    print("Tail : " + str(flip_result.count("Tail")))

elif character1 == 2 :
    flip_result = random.choices(x, k=flips)
    print("Head : " + str(flip_result.count("Head")))
    print("Tail : " + str(flip_result.count("Tail")))

print("""Guess :
1 - Cheater
2 - Real""")

guess1 = int(input())

if guess1 == character1 :
    print("Congrats !!!!")
else :
    print("Program error")