#count vowels and consonants in a string
def func(userInput):
    vowel = "aeiouAEIOU"
    vowelcount = 0
    consonantcount = 0
    for char in userInput:
        if char.isalpha() :
            if char in vowel:
                vowelcount +=1
            else:
                consonantcount +=1
    return vowelcount, consonantcount
vowels,conso = func("My name is Tejas")
print(vowels,conso)
