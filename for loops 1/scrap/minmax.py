def main():
    GrabNumbers()

def GrabNumbers():
    NumList=[]
    SetNumber = int(input("How Many Numbers Will You Add?"))
    ValidNum=False
    while ValidNum==False:
        try:
            NumList.append(input("Please Enter a Number!"))
            Prompt=input("Are you sure about these numbers? Y for yes, otherwise press any key")
            if Prompt=="y" or Prompt=="Y":
                ValidNum=True
        except:
            print("Invalid Input. Please Try Again")
    b=0
    ValidMax=False
    NumMax=NumList[0]
    while b<len(NumList)-1 and ValidMax==False:
        b+=1
        if NumList[b]>NumMax:
            NumMax=NumList[b]
        if b>=SetNumber:
            ValidMax=True
    c=0
    ValidMin=False
    NumMin=NumList[0]
    while c<len(NumList)-1 and ValidMin==False:
        c+=1
        if NumList[c]<NumMin:
            NumMin=NumList[c]
        if c>=SetNumber:
            ValidMin=True
    print("The Biggest Number You Entered Was",NumMax,"The Smallest Number You Entered Was",NumMin)
main()