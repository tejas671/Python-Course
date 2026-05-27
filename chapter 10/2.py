

# class Car:
#     brand = "Scorpio"
# obj1= Car()
# print(obj1.brand)
    

# class Laptop:
#     brand ="default"
#     RAM = "8GB"
#     price = "1 Lakh"
    
# laptop1= Laptop()
# laptop1.brand = "DELL"
# laptop1.RAM = "8 GB"


# laptop2= Laptop()
# laptop2.brand = "HP" #thorugh object we changed attribute value
# laptop2.RAM = "6 GB"

# print(laptop1.RAM, laptop1.price)
# print(laptop2.brand)
# # object_name.attribute_name

# Instance attribute

# class student:
#     college = "VESIT"
#     def __init__(self, name, course):
#         # #constructor
#         # print("whenever a new object is created i am called automatically ")\
#         self.name = name
#         self.course = course
# student1 = student("Khushi", "Maths")
# print(student1.name)
# print(student1.course)

# student2 = student("divya", "science")
# print(student2.name)
# print(student2.course)


class student:
    def __init__(self, name):
        self.name =name
        
    def hello(self):
        print("hello", self.name)
        
s1 = student("saumya")
s1.hello()