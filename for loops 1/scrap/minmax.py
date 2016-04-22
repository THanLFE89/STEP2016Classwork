def main():
    GrabNumbers()

def GrabNumbers():
    NumList=[]
    SetNumber = input("How Many Numbers Will You Add?")
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
    Max=SetNumber[0]
    while b<len(SetNumber)-1 and ValidMax==False:
        b+=1
        if SetNumber[b]>Max:
            Max=SetNumber[b]
        if SetNumber>=1:
            ValidMax=True
    c=0
    ValidMin=False
    Min=SetNumber[0]
    while c<len(SetNumber) and ValidMin==False:
        c+=1
        if SetNumber[c]<Min:
            Min=SetNumber[c]
        if SetNumber>=1:
            ValidMin=True
main()