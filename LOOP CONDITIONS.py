# While Loop Condition

# x=1
# while x<=10:
#     print(x)
#     x=x+1

# output

# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

# y=1
# # x=1
# # while x<=10:
# #     print("hello world",y)
# #     y=y+1

# OUTPUT

# hello world 50705
# hello world 50706
# hello world 50707

# i=1
# while i<=4:
#     print("*")
#     i+=1

# output
# *
# *
# *
# *







# limit = 6

# i=1
# while i<= limit:
#     print("* " * i)
#     i+=1

# output
# * 
# * * 
# * * * 
# * * * *
# * * * * *
# * * * * * *

# i=1
# while i<=5:
#     print("* " * i)
#     i+=1

# output
# * 
#  *  * 
#  *  *  *
#  *  *  *  *
#  *  *  *  *  *

# limit=5
# i=1
# while i<=limit:
    
#     print("*" )
#     i+=1


# a="apple"
# b="grapes"
# print(a,end=" ")
# print(b)

# output
# apple grapes


# limit=5
# i=1
# space=limit
# z=1

# while i<=limit:
#     print(" " * space,end='')
#     print("* "*z)
#     i+=1
#     z+=1
#     space-=1

# output
#      * 
#     * * 
#    * * *
#   * * * *
#  * * * * *

    
# limit=5
# i=1
# z=limit
# space=0
# while i<=limit:
    
#     print(" "*space,end='')
#     print("* "*z)
    
#     space+=2
#     i+=1
#     z-=1

# * * * * * 
#   * * * * 
#     * * *
#       * *
#         *


# a="python"
# print(len(a))

# output
# 6

# num=int(input("enter your number"))
# a=num
# length=(len(str(num)))
# i=0
# result=0
# while i<length:
#     # print(i)
#     # i+=1
#     value=num%10
#     num//=10
#     # print(value)
#     i+=1
#     result+=value**length
# if a== result:
#     print("this is armstrong number")
# else:
#     print("this is not armstrong number")

# x=10
# while x>0:
#     print(x)
#     x=x-1











# x=0
# while x<=10:
#     print(x)
#     x=x+2












# x=1
# while x<=11:
#     print(x)
#     x=x+2


# FOR LoOP

# for a in "python":
#     print(a)

# p
# y
# t
# h
# o
# n

# z="12345678910"
# for a in z:
#     print(a)

# for a in range(10):

#     print(a)

# for a in range(10,20):
#     print(a)

# for a in range(10,21,2):
#     print(a)


# for a in range(10,0,-1):
#     print(a)

# i =10

# for a in range(1,i+1):
#     print("x"*a)

# i=10
# space=i
# for a in range(1,i+1):
#     print(" "*space,end=" ")
#     print("x "*a)
#     space -=1
# c=0
# num=6
# for i in range(1,num+1):
#     if (num % i)==0:
#         c=c+1
# if c==2:
#     print("this is a prime number")
# else:
#     print("not a prime number")
    
# for num in range(1,101):
#     c=0
#     for i in range(1,num+1):
#         if (num % i)==0:
#             c=c+1
#     if c==2:
#         print(num)

# a=["apple","mango","grape","orange"]
# print(a[-1])

# a=["apple","mango","grape","orange"]
# a[0]="banana"
# print(a)

# a=["apple","mango","grape","orange"]
# a.append("banana")
# print(a)

# ['apple', 'mango', 'grape', 'orange', 'banana']
    
    
# a=["apple","mango","grape","orange"]
# a.remove("mango")
# print(a)

# ['apple', 'grape', 'orange']

# a=["apple","mango","grape","orange"]
# # print(a[1:3])
# print(a[::-1])

# ['mango', 'grape']
# ['orange', 'grape', 'mango', 'apple']

# a=["apple","mango","grape","orange"]
# a.insert(1,"grape")
# print(a)

# ['apple', 'grape', 'mango', 'grape', 'orange']

a=["apple","mango","grape","orange"]
for i in a:
    print(i)
