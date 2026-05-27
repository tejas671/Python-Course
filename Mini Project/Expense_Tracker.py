#1
#add expense .append date category description and amount #view prnt, Total spend, Exit option
expenses = []
print(" ")
print("Welcome to Expense Tracker 💸")
print(" ")

while True:
    print("======== MENU =======")
    print("1. Add Expense")
    print("2. View All Expense")
    print("3. View Total Expense")
    print("4. Exit")
    
    choice = int(input("Enter your choice = "))
#add expense
    if (choice==1):
        date = input("Enter date : ")
        category = input("enter the category(food/ travel/ shopping/ medical) : ")
        description = input("enter Details in Brief : ")
        amount = float(input("enter the amount : "))
        expense = {
            "date" : date,
            "category" : category,
            "description" : description,
            "amount" : amount
        }
        expenses.append(expense)
        print("expenses added sucessfully")
    
    elif (choice==2):
        if (len(expenses)==0):
            print("no expense added, go fly some money")
        else:
            print("======= Ye Hai Apka kharcha ========")
            count = 1
            for eachKharcha in expenses:
                print(f"Kharcha number {count} : {eachKharcha["date"]},{eachKharcha["category"]},{eachKharcha["description"]},{eachKharcha["amount"]}")
                count +=1
    elif (choice==3):
        total = 0
        for eachKharcha in expenses:
            total = total + eachKharcha["amount"]
        print("Total Kharcha = ", total) 
            
    elif (choice==4):
        print("Dhanyawad for using our system")
        break
        
else:
    print("Bhak Bewakoof")