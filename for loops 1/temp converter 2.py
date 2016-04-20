def main():
    x=GrabTemp()
    TempConvert(x)

def GrabTemp():
    return float(input("Please Enter Temperature!(Fahrenheit Please!!)"))

def TempConvert(x):
    print("The Temperature in Celsius is",((x-32)*(5/9)),"Degrees" "! Also, the Temperature in Fahrenheit is",x,"Degrees!")
    decision=str(input("Would you like to enter another temperature?(Y/N)"))
    while decision>="y":
        main()
    else:
        print("Thanks for using my program!")
        exit()

main()