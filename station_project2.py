import random
def roll_dice():
    first_dice = random.randint(1, 6)
    second_dice = random.randint(1, 6)
    total = first_dice + second_dice
    print(f"The sum of dice is {first_dice} + {second_dice} = {total}")
    return total
def game():
    winning_numbers = [7, 11]
    casino_numbers = [2, 3, 12]
    goal_numbers = [4, 5, 6, 8, 9, 10]
    first_roll = roll_dice()

    if first_roll in winning_numbers:
        print("You win!")

    elif first_roll in casino_numbers:
        print("The Casino wins!")
    elif first_roll in goal_numbers:
        print("The game continues, your goal is to roll a", first_roll)
        goal = first_roll
        while True:
            new_sum = roll_dice()
            if new_sum==goal:
                print("Winnnn!!!")
                break
            elif new_sum==7:
                print("You rolled 7 before your goal, you lose!")
                break
           
game()   

