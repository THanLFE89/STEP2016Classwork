def main():
    Variables()

def Variables():
    ValidNum=False
    while ValidNum==False:
        try:
            a=float(input("What is the value of A?"))
            b=float(input("What is the value of B?"))
            c=float(input("What is the value of C?"))
            x=float(input("What is the value of X?"))
            print("The proper quadratic equation is:","y = (",a,"x^2 )+","(",b,"x )+","(",c,")","!")
            print("The value of your quadratic is",(a*(x*x))+(b*x)+(c),"!")
            decision=input("Had enough? Then just enter Y. Otherwise..Get off my lawn!")
            if decision=="y" or decision=="Y":
                ValidNum=True
        except:
            print("I don't speak spanish. Try a number instead")
main()