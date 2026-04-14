# class Employee():
#     def __init__(self,name,age,salary):
#         self.name=name
#         self.age=age
#         self.salary=salary

#     def show(self):
#         print(f"name:{self.name}\nage:{self.age}\nsalary:{self.salary}")

# e1=Employee("kiran",20,20000)
# e1.show()
# e1.name="vimal"
# e1.show()


# name:kiran
# age:20
# salary:20000
# name:vimal
# age:20
# salary:20000

# class Employee():
#     def __init__(self,name,age,salary):
#         self.__name = name
#         self.__age = age
#         self.__salary = salary

#     def show(self):
#         print(f"name:{self.__name}\nage:{self.__age}\nsalary:{self.__salary}")

# e1=Employee("manu",21,"10000")
# e1.show()

# e1.__salary=2000000
# e1.show()

# class Bank():
#     def __init__(self,name,amount):
#         self.name=name
#         self.__balance=amount


#     def deposit(self,amount):
#         self.__balance +=amount

#     def withdrawal(self,amount):
         
#         if self.__balance >= amount:
#             self.__balance -= amount
#         else:
#             print("insuficient balance")

#     def show(self):
#         print(f"name:{self.name}\nbalance:{self.__balance}")


# a1=Bank("kiran",1000)
# a1.show()
# a1.deposit(10000)

# a1.balance =100000
# a1.show()
# a1.withdrawal(50000)


# a1.show()


# protect Attribute
 
# class Employee():
#     def __init__(self,name,age):
#         self._name=name
#         self._age=age

# class Employee1(Employee):
#     def show(self):
#         print(f"name:{self._name}\nage:{self._age}")


# a1=Employee1("anu",25)
# a1.show()
    
# class Bank():
#     def __init__(self,name,age,accountnumber):
#         self.name=name
#         self.age=age
#         self.accountnumber=accountnumber

# class Accounts(Bank):
#     def __init__(self, name, age, acno,damount):
#         Bank.__init__(self,name,age,acno)
#         self.__balance=damount

#     def Deposit(self,amount):
#         self.__balance += amount

#     def withdrawal(self,amount):
#         if self.__balance >=amount:
#             self.__balance -=amount
#         else: 
#             print("insufficient balance")

#     def checkbalance(self):
#         print(f"name:{self.name}{" "*10}accountnumber:{self.accountnumber}\nbalance:{self.__balance}")

# s1=Accounts(age=20,name="radha",acno=3556677,damount=2000)

# s1.checkbalance()

# name:radha          accountnumber:3556677
# balance:2000

# Method overriding polymorphism

# class Animal():
#     def sound(self):
#         print("some generic sound")

# class Dog(Animal):
#     def sound(self):
#         print("bark")

# class Cat():
#     def sound(self):
#         print("meow")


# a=Animal()
# a.sound()
# b=Dog()
# b.sound()
# c=Cat()
# c.sound()

# some generic sound
# bark
# meow

# method overloading polymorphism

# class Calculator():
#     def addition(self,a,b=0):
#         print("answer is: ",a+b)

#     def multiply(self,a,b=1):
#         print("answer is: ",a*b)

# a=Calculator()
# a.addition(10)
# a.multiply(20)

# answer is:  10
# answer is:  20

# class Calculator():
#     def addition (self,a,b=0,* args):
#         self.result=a+b
#         for i in args:
#             self.result +=i
#         print("answer is:",self.result)

#     def multiply(self,a,b=1,*args):
#         self.result=a*b
#         for i in args:
#             self.result *=i
#         print("answer is :",self.result)

# # a=Calculator()
# a.addition(10,20,30,40)
# a.multiply(10,2,2,2)



# class Pattern():
#     def __init__(self,n):
#         self.n=n 

#     def show(self):
#         print("Pattern")
#         for a in range (1,a+1):
#             print("*"*a)


# a=Pattern()
# a.show()


# i=5
# space=i
# for a in range(1,i+1):
#     # print(" "*space,end=" ")
#     print ("*"*a)

    
    
#     space-=1



# limit=5
# i=1
# space=limit
# z=1
# while i<=limit:
#     print(" " * space,end='')
#     if i == 1 or i==limit:
#         print("* "*i)
#     else:
#         print("* "+("  "*(i-2))+"*")
#     i+=1
    
#     z+=1
#     space-=1



#      * 
#     * *
#    *   *
#   *     *
#  * * * * * 
 
limit=5
i=1
space=limit
z=1
gap = limit*2
gap-=2
while i<=limit:
    print("* "*i +("  "*(gap)+"* "*i))
    
    gap-=2
    
    
    
    i+=1
    z+=1
    space-=1


    


    

        


        
        










