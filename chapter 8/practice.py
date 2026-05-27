#with keyword


# with open("report2.txt", "r") as f: 
#     data = f.read()
#     print(data)
#     print(data)
# # f.close()

#line by line

# with open("new1.txt","r") as f:
#     line1 = f.readline()
#     line2 = f.readline()
#     print(line1)
    
# with open("new1.txt", "r") as f:
#     read = f.readline()
#     print(read)

# with open("new1.txt","r") as f:
#     lol = f.readlines()
#     print(lol)
#     print(len(lol))
from bisect import bisect_left, bisect_right
arr = [1,2,2,2,3,4]
lower_bound = bisect_left(arr,2)
upper_bound= bisect_right(arr, 2)
print(upper_bound - lower_bound)
print(upper_bound )
print(lower_bound)

