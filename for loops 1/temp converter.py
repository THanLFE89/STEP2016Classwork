def main():
    x=GrabTemp()
    TempConvert(x)
    y=RePrompt()
    Redirect(y)

def GrabTemp():
    return float(input("Please Enter Temperature!(Fahrenheit Please!!)"))

def RePrompt():
    return str(input("Would you like to enter another temperature?(Y/N)"))

def Redirect(y):
    if y>="y":
        main()
    else:
        print("Thanks for using my program!")

def TempConvert(x):
    while x<=1000 and x>=-459.67:
        print("The Temperature in Celcius is",((x-32)*(5/9)),"Degrees" "! Also, the Temperature in Fahrenheit is",x,"Degrees")
        x+=1
        break

main()