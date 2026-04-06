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



class Employee():
   def add(self,name,age):
      self.name=name
      self.age=age

class Role():
   def add1(self,role,salary):
      self.role=role
      self.salary = salary


class c(Employee,Role):
   def show(self):
        print(f"name:{self.name}\nage:{self.age}\nrole:{self.role}\nsalary:{self.salary}")


p=c()
p.add("abhi",25)
p.add1("developer","25000")


p.show()