import random
def main():
  dice_rolls = int(input('How many dice would you like to roll? '))
  dice_size = int(input('How many sides are the dice? '))
  dice_sum = 0
  for i in range(0, dice_rolls):
    roll = random.randint(1, dice_size)
    if roll == 1:
      print(f'You rolled a {roll}! Better luck next time!')
    elif roll == dice_size:
      print(f'You rolled a {roll}! Bingo!')
    else:
      print(f'You rolled a {roll}')
    dice_sum += roll
  print(f'You have rolled a total of {dice_sum}')

if __name__== "__main__":
  main()