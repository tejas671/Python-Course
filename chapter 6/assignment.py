#countdown timer
import time

count = int(input("enter number = "))
print("countdown starts in ")
time.sleep(2)
for i in range(count, 0, -1):
    print(i)
    time.sleep(1)
print("WOhoooooo, Happy new year")