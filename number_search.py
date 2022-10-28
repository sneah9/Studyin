import random

def guess_random_number(tries, start, stop):
    target = random.randint(start, stop)
    while tries >0:
        print("You have", tries, "tries remaining.")
        guess = int(input(f"Guess a number between {start} and {stop}:"))
        if guess == target:
            print("You have successfully guessed! The target number was:", target)
            return
        elif guess > target:
            print("Guess lower!")
        elif guess < target:
            print("Guess higher!")
        tries -=1
    print("You have run out of tries to guess the target number of:", target)

def guess_random_num_linear(tries, start, stop):
    target = random.randint(start, stop)
    print("The target number is", target)
    while (tries > 0):
        for x in range (start, stop,1):
            print("The program is guessing...", x)
            if x == target:
                print("You have successfully guessed! The target number was:", target)
                return x
            tries -=1
            if tries <1:
                break
            print("you have", tries, "attempts left.")
    print("You have run out of tries to guess the target number of:", target)
    return

def guess_random_num_binary(tries, start, stop):
    target = random.randint(start, stop)
    print("The target number is", target)
    our_list = list(range(start, stop, 1))
    #while:
    lower_bound = start
    upper_bound = stop

    while lower_bound <= upper_bound and (tries > 0):
        pivot = (lower_bound + upper_bound) // 2
        pivot_value = our_list [pivot]
        print("The program is guessing...", pivot_value)

        if pivot_value == target:
            print("You have successfully guessed! The target number was:", target)
            return pivot
        if pivot_value > target:
            print("This guess was too large")
            upper_bound = pivot - 1
        else:
            print("this guess was too small")
            lower_bound = pivot + 1
        tries -=1
    print("Your program failed to find the number.")

    


guess_random_number(10, 0, 10000)
#guess_random_num_linear(200, 0, 200)
#guess_random_num_binary(10, 0, 200)


#guess_random_number(tries, start, stop)