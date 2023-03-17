import random
import numpy as np

x = ["Head", "Tail"]

def coin_flips() :

    total_head = 0
    total_tail = 0
    margin = 0
    number = 0
    
    while number < 1000 :

        weightage1 = random.randint(1,100)
        weightage2 = random.randint(1,100)

        flip_result1 = random.choices(x, weights = (weightage1,weightage2), k = 100000)

        if flip_result1.count("Head") > flip_result1.count("Tail") :
            total_head += 1
        else :
            total_tail += 1
    
        difference_in_number = flip_result1.count("Head") - flip_result1.count("Tail")
        margin += difference_in_number
        number += 1

    print("MAT " + str(total_head))
    print("No MAT " + str(total_tail))
    print("Margin of difference " + str(margin))

coin_flips()

print("Banana Bread")