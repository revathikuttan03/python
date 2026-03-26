# without argument without return

# def demo():
#     print("hello world")

# demo()
# demo()

# hello world
# hello world

# with argument without return

# def add1 (a,b): #parameter
#     print(a+b)

# add1(10,30) #argument
# add1(50,70)

# output

# 40
# 120

# with argument with return

# def mul(a,b):
#     c=a*b
#     return c
# a=mul(10,5)
# print(a)

# without argument with return

# def text():
#     return "python is a programming language"
# a = text()
# print(a)

# default argument

# def add(a=0,b=0,c=0):
#     print(a+b+c)
# add()

# output
# 0

# keyword argument

# def my_data(name="",age=0,place=""):
#     print("name:",name)
#     print("age:",age)
#     print("place:",place)
# # my_data("kiran",12,"thrissur")
# my_data(age=25,name="hari",place="kottayam")

# name: hari
# age: 25
# place: kottayam

# def add(*args):
#     # print(args)
# # #     print(type(args))
# # add(10,20,30,40,50,60,70,80)
#       for i in args:
#         print(i)
# add(10,20,30,40,50,60,70,80)

# def add(*args):
#     sum=0
#     for i in args:
#         sum=sum+i
#     print(sum)
# add(10,20,30,40,50,60,10)

# output
# 220

# def details(**kwargs):
   
#     for key,value in kwargs.items():
#         print(key,value)
# details(name="kiran",age=25,place="thrissur")

# output

# name kiran
# age 25
# place thrissur

# def percentage(total_mark=0,my_mark=0):
#     p = (my_mark/total_mark)*100
#     print(f"percentage is :{int(p)}%")
# percentage(100,60)

# output
# percentage is :60%


# def pattern(a):
#     space=a
#     for i in range(a):
#         print("* "*i)
#         print(" "*space,end=" ")
#         space-=1

# pattern(7)

# output
#         * 
#        * *
#       * * *
#      * * * *
#     * * * * *
#    * * * * * *

# recursive fuction

# def fact(x):
#     f=1
#     for i in range(1,x+1):
#         f=f*i
#     print(f)
# fact(6)

# output
# 720

# def fact(x):
#     if x==1:
#         return 1
#     else:
#         return x * fact(x-1)
# a=fact(5)
# print(a)

# output
# 120

# def count(x):
#     print(x)
#     if x==1:
#         return 1
#     else:
#         return count(x-1)
# count(10)

# def count(y=1):
#     print(y)
#     return count(y+1)
# count(10)

# def count(x,y=1):
#     print(y)
#     if x==1:
#         return 1
#     else:
#         return count(x-1,y+1)
# count(10)

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

# lambda function

a=lambda : print("hello world")
a()

    

    

    

      

