
# class student:
#     def __init__(self, name, listofmarks):
#         self.name = name
#         self.listofmarks = listofmarks
        
#     def average(self):
#         sum = 0
#         for eachmarks in self.listofmarks:
#             sum = sum + eachmarks
#         average = sum / 3
#         print(average)
        
# student1 = student("Tejas", [12,17,31])
# student1.average()

class student:
    @staticmethod
    def evenandodd(num):
        if num % 2==0:
            print("even")
        else:
            print("odd")
student.evenandodd(12)          

# abstraction:
#     showing only essential details, hiding internal complexity
# encapsulation :
#     wrapping data +methods inside a single unit (class)
#inheritance : 
    # one class gets properties and methods of another class
#Polymorphism :
    # same name but different behaviour 