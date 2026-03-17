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

# output
# 2
# 3 
# 5 
# 7 
# 11
# 13
# 17

# a=["apple","mango","grape","orange"]
# print(a[-1])

# orange

# a=["apple","mango","grape","orange"]
# a[0]="banana"
# print(a)

# output
# ['banana', 'mango', 'grape', 'orange']

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

# a=["apple","mango","grape","orange"]
# for i in a:
#     print(i)

# output
# apple
# mango
# grape
# orange

# num=int(input("enter your number"))

# a=num
# length=(len(str(num)))

# result=0
# for i in range (length):
#         value=num%10
#         num//=10
#         result+=value**length
# if a==result:
#     print("this is armstrong number")

# else:
#     print("this is not armstrong number")



# for i in range(1,6):
#      print()
#      for c in range(1,i+1):
#           print(c , end='')

# TUPLE

# a=("apple","orange")
# print(a[0])
     
    
# a="apple",3.14,10,True
# print(a)
# print(type(a))

# ('apple', 3.14, 10, True)
# <class 'tuple'>

# a="apple",3.14,10,True
# print(len(a))

# 4

# a="apple",3.14,10,True
# for i in a:
#     print(i)

# apple
# 3.14
# 10
# True

# LOOP CONTROL FLOW STATEMENT

# 1. CONTINUE
# for i in range(5):
#     if i==3:
#         continue
#     print(i)

     
# 0
# 1
# 2
# 4

# for i in range(5):
#      if i==3:
#         pass
#      print(i)

# for i in range(5):
#      if i==3:
#         break
#      print(i)

# 0
# 1
# 2

# tuple

# a=("apple","grape","lemon")
# a=list(a)
# a[0]="banana"
# a=tuple(a)
# print(a)
# print(type(a))

# set

# a={"apple","banana","grape","orange","apple"}
# print(a)

# a={5,1,4,3,6,2}
# print(a)

# {1, 2, 3, 4, 5, 6}

# a=["red","blue","gray","black","red"]
# a=set(a)
# print(a)
# print(type(a))

# {'black', 'gray', 'red', 'blue'}
# <class 'set'>

# a={"red","blue","gray","black"}
# a.add("green")
# print(a)

# {'blue', 'black', 'gray', 'red', 'green'}

# a={"red","blue","gray","black"}
# b={"banana","apple","orange"}
# a.update(b)
# print(a)

# {'apple', 'black', 'red', 'orange', 'banana', 'blue', 'gray'}

# a={"red","blue","gray","black"}
# a.remove("red")
# print(a)

# a={"red","blue","gray","black"}
# a.discard("green")
# print(a)

# a={"red","blue","gray","black"}
# x=a.pop()
# print(x)
# print(a)

# blue
# {'gray', 'black', 'red'}

# a={"red","blue","gray","black"}
# a.clear()
# print(a)

# set()

# a={"red","blue","gray","black"}
# del a
# print(a)

# a={"red","blue","gray","black"}
# for i in a:
#      print(i)

# gray
# black
# red
# blue

# a={'red','black','white','green'}
# b={'red','yellow','blue','black'}
# c=a.union(b)
# print(c)

# {'white', 'black', 'yellow', 'red', 'green', 'blue'}

# a={'red','black','white','green'}
# b={'red','yellow','blue','black'}
# c=a|b
# print(c)

# {'green', 'yellow', 'blue', 'black', 'red', 'white'}

# set union

# a={'red','black','white','green'}
# b={'red','yellow','blue','black'}
# c={'yellow','gray','orange','black'}
# d=a.union(b,c)
# print(d)

# {'blue', 'gray', 'green', 'red', 'orange', 'black', 'yellow', 'white'}

# a={'red','black','white','green'}
# b={'red','yellow','blue','black'}
# c=a.intersection(b)
# print(c)

# {'black', 'red'}

# a={'red','black','white','green'}
# b={'red','yellow','blue','black'}
# c=a&b
# print(c)

# {'red', 'black'}

# a={'red','black','white','green'}
# b={'red','yellow','blue','black'}
# c=a.difference(b)
# print(c)

# {'green', 'white'}

# a={'red','black','white','green'}
# b={'red','yellow','blue','black'}
# c=a-(b)
# print(c)

# {'white', 'green'}

# a={'red','black','white','green'}
# b={'red','yellow','blue','black'}
# c=a.symmetric_difference(b)
# print(c)

# {'green', 'yellow', 'white', 'blue'}

# a={'red','black','white','green'}
# b={'red','yellow','blue','black'}
# c=a^(b)
# print(c)

# {'yellow', 'white', 'green', 'blue'}

# DICTIONARY DATA TYPE

# a={"name":"kiran","age":27,"place":"thrissur"}
# print(a)
# print(type(a))

# {'name': 'kiran', 'age': 27, 'place': 'thrissur'}
# <class 'dict'>

# a={"name":"kiran","age":27,"place":"thrissur"}
# print(a['age'])

# 27

# a={"name":"kiran","age":27,"place":"thrissur"}
# a["age"]=25
# print(a)

# {'name': 'kiran', 'age': 25, 'place': 'thrissur'}

# a={"name":"kiran","age":27,"place":"thrissur"}
# a["job"]="developer"
# print(a)

# {'name': 'kiran', 'age': 27, 'place': 'thrissur', 'job': 'developer'}