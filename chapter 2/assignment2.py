#temp
C = float(input("enter temp in celsius: "))
fahrenheit = (C * (9/5))+ 32
kelvin = C + 273.15
print(fahrenheit)
print(kelvin)

#Bill split
total = float(input("total_bill_amount: "))
count = int(input("enter number of Freinds: "))
pay = total / count
print("each friend will pay: ",pay, type(pay))