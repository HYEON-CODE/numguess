from random import randint
from time import sleep

def game_start():
    # answer range 1~100
    answer = randint(1,100)
    trial = 10 # 게임 반복 횟수
    base_score=[100]

    # Print answer
    print(answer)

    # User interaction
    username = input("Hi there, What is your name?")
    print(f"Hi,{username}! Please be my guest!!")

    # Compare answer with user's guess
    while trial>1:
        trial-=1
        guess = int(input(f"So {username}, Guess the number(1-100): "))
        if answer==guess:
            print(f"Wow! Your got is right!! The answer is {answer} bonus score+{trial+1}")
            break
        elif guess>answer:
            print(f"Keep going, That was too high. \nchance left:{trial}")
        elif guess<answer:
            print(f"Keep going, That was too low \nchance left:{trial}")
    new_score=[i+trial+1 for i in base_score]
    print(f"your score is {new_score}")
game_start()