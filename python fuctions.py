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

    

    

      

