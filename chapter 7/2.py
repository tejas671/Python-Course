# #funcion defintion with paramnetr
# def average(a,b):
#     averageValue = (a+b)/2
#     print(averageValue)    
# #function calling arguments
# average(5,10)
# average(3,10)
# average(10,9)
# # average()


# def show_age(name, age):
#     print(f"{name} is {age} Years Old")
    
# show_age("Tejas Sharma", 22)


# def add_numbers(a, b):
#     sum = a+b
#     difference = a - b
#     print(sum, difference)
# add_numbers(10, 5)

# def fav_food(food):
#     print(f"Tejas loves <{food}>")
# fav_food("Vada pav")

# #RETURN STATEMENT
# # send value back from a function

# def multiply(a=10,b=9):
#     return a*b
# result = multiply(5,10)
# print(result)
# print(multiply())
# #Function defintion with PArameter
# # def average():

# def square(num=10):
#     return num**2

# print(square(5))
# print(square(10))
# print(square(8))   

# print(square())


def func(userInput):
    vowels = "aeious"
    countvowel = 0
    countconsonant = 0
    for eachChar in userInput:
        if (eachChar.isalpha()):
            if eachChar in vowels:
                countvowel +=1
            else :
                countconsonant +=1    
    return countvowel, countconsonant 
vowels, consonants = func("Hellow there i am Tejas ka Interpretor")

print(vowels, consonants)