import random

def guess(x):
    rand_num = random.randint(1,x)
    guess_num = 0
    while(guess_num != rand_num):
        guess_num = int(input(f"guess a number between 1 and {x}: "))

        if guess_num<rand_num:
            print("sorry, guess again too low")
        elif guess_num>rand_num:
            print("sorry, guess again too high")
    print(f"congrats you have guessed the number {rand_num} correctly")    

def pc_guess(x):
    lowest = 1
    highest = x
    feedback = ''
    while feedback != 'c':
        if lowest != highest:
            guess_num = random.randint(lowest, highest) 
        else: 
            guess_num = lowest
        feedback = input(f'is {guess_num} too high (H), too low (L), or correct (C)? ').lower()
        if feedback == 'h':
            highest = guess_num - 1
        if feedback == 'l':
            lowest = guess_num + 1
    print(f'The computer guessed the number {guess_num} correctly!')

pc_guess(1000)