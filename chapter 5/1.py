#dictionary and set in python
student = {"name" : "tejas",
           "age": 23,
           "city": "Mumbai",
           "roll_no": 103,
           "name": "gudiya"
           }
print(type(student))
print(student)
print(student["city"])

student["city"] = "Pune"
student["country "] = "India"
print(student)
student.pop("roll_no")
print(student)
print(student.keys())
print(student.values())
print(student.items()) # rewrites as tuple
print(student.get("name"))