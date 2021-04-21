import random
def main():

    print('You rolled a die')
    dice_rolls = int(input("Enter the no of dice rolling"))
    dice_size = int(input("Enter no of sides of the dice"))
    dice_sum = 0
    for i in range(0,dice_rolls):
        roll = random.randint(1,dice_size)
        dice_sum+= roll
        if roll == 1:
            print(f"you rolled a {roll}! Critical fail")
        elif roll == dice_size:
            print(f"yo rolled a {roll}! Critical Success")
        else:
            print(f"you rolled a {roll}")
    print(f"Sum of the dice is {dice_sum}")



if __name__== "__main__":
  main()