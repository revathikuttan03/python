def add(a,b):
    print(a+b)

def mul(a,b):
    print(a*b)

def pattern(a):
    space=a 
    for i in range(1,a+1):
        print("* "*i)
        print(" "*space,end=" ")
        space-=1

