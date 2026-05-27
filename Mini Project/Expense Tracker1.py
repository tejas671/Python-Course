
print("Welcome Buddy to Your Very Own Expense Tracker")
print(" ")
expenses = []

while True:
    print("====================== Menu =======================")
    print("1. Add Expenses")
    print("2. View all Expense")
    print("3. View Total Expense")
    print("4. Exit")
    
    choice = int(input("Enter Your Choice = "))
    
    if (choice==1):
        date = input("Enter Date :")
        category = input("Enter the category (Food / Travel / Shopping / Medical): ")
        Details = input("Enter Details in Brief = ")
        amount = float(input("Enter The Amount : "))
        
        expense = {
            "date" : date,
            "category" : category,
            "details" : Details,
            "amount" : amount
        }
        expenses.append(expense)
        print("Expenses Added Sucessfully😁")

    elif (choice ==2):
        if (len(expenses)) == 0:
            print("pls add something in the list")
        else :
            print("=========Your Expense List ============")
            count = 1
            for ESpending in expenses:
                print(f"Your Expenditure Number {count} : \nDate : {ESpending['date']}, \nCategory : {ESpending['category']}, \nDetails : {ESpending['details']}, \nAmount : {ESpending['amount']}")
                count+=1
            print("Expenses Viewed Sucessfully😁")
    
    elif (choice ==3):
        total = 0
        for ESpending in expenses:
            total = total + ESpending["amount"]
            
        print("Total amount : ", total)
        
    elif (choice==4):
        print("Dhanyawad")
        break
    else:
        print("kuch toh sharam karo")
        