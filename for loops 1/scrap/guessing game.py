import random

def main():
    Compare()

def Compare():
    try:
        b=2
        Answer = random.randint(1,10)
        print(Answer)
        ValidGuess=False
        while ValidGuess==False:
            Guess = int(input("Feelin' Lucky, Punk??"))
            if Answer==Guess:
                print("Lucky Guess! Now Scram!!")
                ValidGuess=True
            elif b <= 0:
                print("There's only room for 1 coder in this integrated development environment")
                print("BANG")
                print("GAME OVER")
                ValidGuess = True
            elif Guess==Answer+1 or Guess==Answer-1:
                print("You're steaming hot!")
            elif Guess==Answer+2 or Guess==Answer-2:
                print("You're getting warmer..")
            else:
                print("Are you even trying?!")
            b-=1
    except:
        print("Nice Try.")
main()