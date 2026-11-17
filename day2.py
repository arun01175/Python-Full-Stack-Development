# # # # # # # def new_func():
# # # # # # #     def add(a,b):
# # # # # # #         result=a + b
# # # # # # #         print(result)
# # # # # # #     add(10,20)
# # # # # # #     add(50,30)

# # # # # # # for i in range(0):
# # # # # # #     print("good morning students!")

# # # # # # #     i = 1
# # # # # # #     while i <=5:
# # # # # # #         print("good morning students!")
# # # # # # #         i += 1 

# # # # # # #         def greet():
# # # # # # #             print("hello students")
# # # # # # #             print("welcome to python programming  ")
# # # # # # #             greet()

# # # # # # # students =["john","jane","jack","jill"]
# # # # # # # print(students)
        
# # # # # # # students =["john","jane","jack","jill"]
# # # # # # # students.append("james")
# # # # # # # students.remove("jill")
# # # # # # # students.insert(2,"james")
# # # # # # # print(students)
# # # # # # #######tuples#####
# # # # # # students_details=("john",20,"male")
# # # # # # print(students_details[0])


# # # # # student ={
# # # # #     "name":"john",
# # # # #     "age":22,
# # # # #     "marks":95,
# # # # #     "passed":True,
# # # # #     "usn":"1gd25cs400",
# # # # #     "collage":"goplan college of enginnering and management",
# # # # #     "address":"hoodi"
# # # # #     }

# # # # # student["cource"]="python programming"
# # # # # print(student["name"])
# # # # # print(student["cource"])
# # # # # print(student["marks"])
# # # # # print(student["collage"])
# # # # # print(student["address"])
# # # # # print(student["usn"])

# # # # # class Student:
# # # # #     def display(self):
# # # # #         print("hello students")
# # # # #         print("welcome to python programming")

# # # # # s1= Student()
# # # # # s1.display()

# # # # # class teacher:
# # # # #     def display(self):
# # # # #         print("hello teachers")
# # # # #         print("welcome to india") 

# # # # # t1 = teacher()
# # # # # t1.display()
# # # # # class student:
# # # # #     def __init__(self,name,age,marks):
# # # # #         self.name=name
# # # # #         self.age=age
# # # # #         self.marks=marks

# # # # #     def display(self):
# # # # #         print("name:",self.name)
# # # # #         print("age:",self.age)
# # # # #         print("marks:",self.marks)
# # # # #         s1=student("john",20,95)
# # # # #         s2=student("jane",22,90)
# # # # #         s1.display()
# # # # #         s2.display()

# # # # class Student:
# # # #     def __init__(self):
# # # #         self.__marks = 90

# # # #     def show_marks(self):
# # # #         print("Student Marks:", self.__marks)

# # # # s1 = Student()

# # # # s1.show_marks()

# # # # class Bank:
# # # #     def __init__(self):
# # # #         self.__balance = 1000

# # # #     def deposit(self, amount):
# # # #         self.__balance += amount

# # # #     def display(self):
# # # #         print("Balance:", self.__balance) 

# # # # b1 = Bank()

# # # # b1.deposit(500)
# # # # b1.display()
 
# # # class Father:
# # #     def house(self):
# # #         print("Father has a house")


# # # class Son(Father):
# # #     def bike(self):
# # #         print("Son has a bike")

# # # s1 = Son()

# # # s1.house()
# # # s1.bike()


# # # class Grandfather:
# # #     def house(self):
# # #         print("Grandfather has a house")

# # # class Father(Grandfather):
# # #     def car(self):
# # #         print("Father has a car")

# # # class Son(Father):
# # #     def bike(self):
# # #         print("Son has a bike")

# # # s1 = Son()

# # # s1.house()
# # # s1.car()
# # # s1.bike()


# # class Father:
# #     def house(self):
# #         print("Father has a house")


# # class Son(Father):
# #     def bike(self):
# #         print("Son has a bike")

# # class Daughter(Father):
# #     def car(self):
# #         print("Daughter has a car")


# # s1 = Son()
# # d1 = Daughter()

# # s1.house()
# # s1.bike()

# # d1.house()
# # d1.car()    

 
# # class Dog:
# #     def sound(self):
# #         print("Dog barks")

# # class Cat:
# #     def sound(self):
# #         print("Cat meows")


# # d1 = Dog()
# # c1 = Cat()

# # d1.sound()
# # c1.sound()  
# from abc import ABC, abstractmethod


# class Car(ABC):

#     @abstractmethod
#     def start(self):
#         pass


# class BMW(Car):

#     def start(self):
#         print("BMW car starts with a button")


# c1 = BMW()
# c1.start()                                          