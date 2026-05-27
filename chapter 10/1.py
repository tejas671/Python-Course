class student:
    name = "Tejas"
    gender = "Male"
    division = "B"
s1= student()
print(s1.name)

class vehicle:
    color = "black"     #attribute 1
    engine = "petrol"   #attribute 2
    milage = "25"       #attribute 3
    
    def start(self):
        print("When you press clutch and acceleration")
    
    
    
    
car = vehicle()  #object creation
bike = vehicle()
aeroplane = vehicle()

print(car.color)

class Residential:
    Building = "Red"
    Bunglow = "Brick red"
    chawl = "white"
    rowhouse = "white-red"
ghar = Residential()
print(ghar.chawl)