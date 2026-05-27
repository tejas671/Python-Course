#1

dict1 = {"azure": "Blue color",
         "sophisticated": "advanced, fancy",
         "python": "snake, programming language"}
print(dict1)
#2
numb1 = {1,2,3,4}
numb2 = {2,4,6,7}
openai = numb1.union(numb2)
print(openai)
close = numb1.intersection(numb2)
print(close)

#3
girl = {2,6,4,3,2,10}
girl.add(9)
print(girl)
girl.add('9.0')
print(girl)
