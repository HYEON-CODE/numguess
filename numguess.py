from random import randint
from time import sleep

def game_start():
    # answer range 1~100
    answer = randint(1,100)
    game_count = 10 # 게임 반복 횟수

    # Print answer
    print(answer)

    # User interaction
    username = input("Hi there, What is your name?")
    print(f"Hi,{username}! Please be my guest!!")

    # Compare answer with user's guess
    while game_count>1:
        guess = int(input(f"So {username}, Guess the number(1-100): "))
        game_count-=1
        if answer==guess:
            print(f"Wow! Your got is right!! The answer is {answer}\n")
            break
        elif guess>answer:
            print(f"Keep going, That was too high. \nchance left:{game_count}")
        elif guess<answer:
            print(f"Keep going, That was too low \nchance left:{game_count}")

game_start()