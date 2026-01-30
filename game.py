import random
import time

print("""

    rock-paper-scissor game
      
      please choose one of them:
      1-rock
      2-scissor
      3-paper
      4-exit game

      rules:
      1-rock beats scissor
      2-scissor beats paper
      3-paper beats rock

      have fun!

    """)
while True:
    user_1 =int(input("your choose: "))
    if user_1 == 4:
        print("gameover!")
        break
    elif user_1>=5:
        print("please choose 1to 4!")
    else:
        game = {1:"rock",2:"scissor",3:"paper"}
        AI_1=random.randint(1,3)
        AI=game.get(AI_1)
        user = game.get(user_1)

        if user == "rock" and AI =="scissor":
            time.sleep(0,1)
            print("i choose scissors, YOU  win!")
        elif user == "rock" and "paper":
            time.sleep(0.1)
            print("i choose paper , you loose!")

        elif user == "paper" and AI == "rock":
            time.sleep(0.1)
            print("i choose rock, you win!")

        elif user == "paper" and AI=="scissor":
            time.sleep(0.1)
            print("i choose scissor,you lose!")

        elif user =="scissor" and AI == "paper":
            time(0.1)
            print("i choose paper, you Win!")

        elif user =="scissor" and AI == "rock":
            time(0.1)
            print("i choose rock,you lose!")

        else:
            print("draw. Please continue.")


       

