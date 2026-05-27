#1
# 

#2
marks = (87, 64, 33, 95, 76)
print(max(marks))
print(min(marks))

#3
mark = int(input("enter your marks:"))

if mark>= 85:
    print("A")
elif mark>= 75:
    print("B")
elif mark>= 65:
    print("C")
elif mark >= 55:
    print("D")
else:
    print("fail")