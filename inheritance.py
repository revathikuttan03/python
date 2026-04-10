# class Employee_Details():
#     def add (self,employee_name,employee_age):
#         self.en=employee_name
#         self.ea=employee_age
    

# class Employee(Employee_Details):
#     pass
        


# class Employee_role(Employee):
#     def add_role(self,role):
#         self.role=role
#     def show(self):
#         print(f"name:{self.en}\nage:{self.ea}\nrole:{self.role}")



# p2= Employee_role()
# p2.add("yadav",30)
# p2.add_role("developer")

# p2.show()

# name:yadav
# age:30
# role:developer



# class Employee():
#    def add(self,name,age):
#       self.name=name
#       self.age=age

# class Role():
#    def add1(self,role,salary):
#       self.role=role
#       self.salary = salary


# class c(Employee,Role):
#    def show(self):
#         print(f"name:{self.name}\nage:{self.age}\nrole:{self.role}\nsalary:{self.salary}")


# p=c()
# p.add("abhi",25)
# p.add1("developer","25000")


# p.show()

# class Bank_account():
#     def add(self,holder_name,balance):
#         self.hn=holder_name
#         self.balance=balance


# class Details():
#     def add1(self,deposit,withdraw):
#         self.deposit=deposit
#         self.withdraw=withdraw
      

# class c(Bank_account,Details):
#     def show(self):
        

# class A():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def show(self):
#         print("This is class A")
#         print("name:",self.name)
#         print("age: ",self.age)

# class B(A):
#     pass



# class C(A):
#     def show(self):
#         print("This is class C")
#         print("name:",self.name)
#         print("age: ",self.age)


# s1=C("anu",20)
# s1.show()
        
# This is class C
# name: anu
# age:  20


class Person():
    def add(self,name,age):
        self.name=name
        self.age=age

class Employee(Person):
    def add1(self,role):
        self.role=role

class Project():
    def add2(self,project_name):
        self.pn=project_name


class Team(Employee,Project):
    def show(self):
        print(f"name:{self.name}\nage:{self.age}\nrole:{self.role}\nproject_name:{self.pn}\n")


s1=Team()
s1.add("manu",20)
s1.add1("developer")
s1.add2("python")
s1.show()

    
        
        



        
        


