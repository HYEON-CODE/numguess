from random import randint
from time import sleep

# answer range 1~100
answer = randint(1,100)

# Print answer
print(answer)

# User interaction
username = input("Hi there, What is your name?")
print(f"Hi,{username}! Please be my guest!!")
guess = int(input(f"So {username}, Guess the number(1-100): "))
print(f'Well choice {username}~~ You picked {guess}!!')

# Compare answer with user's guess
if answer==guess:
    print("************************")
    sleep(1)
    print("************************")
    sleep(1)
    print("************************")
    sleep(1)        
    print(f"Wow! Your got is right!! The answer is {answer}")
elif guess>answer:
    print(f"Keep going, That was too high")
elif guess<answer:
    print(f"Keep going, That was too low")