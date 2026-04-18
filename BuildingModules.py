# import math
# a=90
# b=math.factorial(a)
# print(b)


# import random
# a=random.randint(1,100)
# print(a)

# output
# random number 36,12,55

# import random
# a=random.random()
# print(a)

# 0.7784

# import random
# a=random.randrange(0,100,2)
# print(a)

# import random
# a=["apple","banana","grape","orange"]
# b=random.choice(a)
# print(b)

# output 
# apple

# import random

# a=[{'id':1,'name':"rayees",'place':"thrissur"},{'id':2,'name':"anu",'place':"trivandrum"},{'id':3,'name':"kiran",'place':"ernklm"}]
# b=random.choice(a)
# print("id :",b['id'])
# print(b['name'])
# print(b['place'])

# id : 3
# kiran
# ernklm

# import datetime
# a=datetime.date.today()
# print(a)

# 2026-04-14

# import datetime
# a=datetime.date.today()
# b=datetime.date(year=1998,month=3,day=29)
# # print(a.strftime("%H:%M:%S"))
# print((a-b).days)

# a=datetime.date.today()
# b=datetime.timedelta(days=10)
# print(a+b)

# class Employee ():
#     def add (self,name,age,place):
#         self.name=name
#         self.age=age
#         self.place=place
#     def show(self):
#         print(f"name:{self.name}\nage:{self.age}\nplace:{self.place}")

# a=Employee()
# a.add("kiran",20,"thrissur")
# a.show()

import datetime  
x= True
data = []
while x:
    choice = input("enter your choice:(add,display,exit):")
    match choice:
        case "add":
            a=input("enter your name: ")
            b=input("enter your place: ")
            c=datetime.datetime.now()
            data.append({'name':a,'place':b,'time':c})
        
        case 'display':
            for i in data:
                v = i['time']
                
                print("name: ",i['name'])
                print("place: ",i['place'])
                print("time:", i['time'].strftime("%H:%M:%S"))
                print("----------------------------------------")
        case 'exit':
            x= False
        
   




