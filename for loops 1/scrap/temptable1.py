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
            #the anti-evan code