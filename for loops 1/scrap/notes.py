'''
Mystring="Apple"
count=len(Mystring)
print(count)
for a in range(0,count):
    print(Mystring[a])

Mystring="Apple"
count=len(Mystring)
print(count)
for a in range(0,count):
    print(Mystring[a])
c=0
while c<count:
    print(Mystring[c],end=" ")
    c+=1
'''
'''
def main():
    x=0
    b=(x-32)*(5/9)
    c=(9/5)*x+32
    CelsiusTable(x)
    print(" ")
    x=0
    FahrTable(x)

def CelsiusTable(x):
    for x in(0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100):
        print((x-32)*(5/9),end=" ")
        if x>=96:
            x=False
        else:
            x+=5

def FahrTable(x):
    for x in(0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100):
        print((9/5)*x+32,end=" ")
        if x>=96:
            exit()
        else:
            x+=5

main()
'''
'''
def main():
    iterations=getiterations()
    getaverage(iterations)

def getiterations():
    return int(input("How Many Numbers Will You Add?"))

def getaverage(y):
    firstlist=[]
    for a in range(0,y):
        testscore=int(input("Enter your test score?"))
        firstlist.append(testscore)
    lengthofList=len(firstlist)
    sum=0
    print("The numbers you entered were:",end=" ")
    for c in range(0,lengthofList):
        print(firstlist[c],end=" ")
        sum=sum+firstlist[c]
    firstlist.append(100)
    sum=sum+firstlist[lengthofList]
    print("")
    print("The average of your numbers is",sum/(lengthofList+1))

    for b in firstlist:
        print(b)

main()

'''
def main():
    NamesColors()
'''
def NamesColors():
    namelist=[]
    colorlist=[]
    exit=False
    while exit==False:
        namelist.append(input("Enter Your Name"))
        colorlist.append(input("Enter Your Favorite Color"))
        decision=input("Press Q to Quit or any other key to Continue")
        if decision=="q" or decision=="Q":
            exit=True
    length=len(namelist)
    for a in range(0,length):
        print(namelist[a],"'s Favorite Color is",colorlist[a],"!")

main()
'''
def main():
    try:
        x=input("Give me your age")
        print(x)
    except:
        print("Why you no give me a digit?")
main()