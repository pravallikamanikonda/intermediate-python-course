import random
def main():

    print('You rolled a die')
    dice_rolls = 2
    dice_sum = 0
    for i in range(0,dice_rolls):
        roll = random.randint(1,6)
        print(f"You rolled a {roll}")
        dice_sum+= roll
    print(f"Sum of the dice is {dice_sum}")



if __name__== "__main__":
  main()