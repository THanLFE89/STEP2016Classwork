import random

def main():
    Compare()

def Compare():
    b=2
    Answer = random.randint(1, 10)
    print(Answer)
    ValidGuess=False
    while ValidGuess==False:
        Guess = int(input("Feelin' Lucky??"))
        if Answer==Guess:
            print("Lucky Guess!")
            ValidGuess=True
        elif Guess==Answer+1 or Guess==Answer-1:
            print("You're steaming hot!")
        elif Guess==Answer+2 or Guess==Answer-2:
            print("You're getting warmer..")
        elif b<=0:
            print("Sorry bruh. Game Over")
            ValidGuess=True
        else:
            print("You're cold-blooded, bro")
        b-=1
main()