f=open("classtestfile.txt", "r")
myList=[]
for line in f:
    myList.append(line)
b=len(myList)
for a in range(0,b):
    print(myList[a])

#reads should always be under a try/except function
