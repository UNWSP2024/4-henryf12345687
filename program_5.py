# Program #5: Bank Balance
# Write a program that asks the user to enter the amount that he or she has budgeted for a month.
# A loop should then prompt the user to enter each of his or her expenses for the 
# month and keep a running total. (Enter 0 to exit the loop)  
# When the loop finishes, the program should display the amount that the 
# user is over or under budget.

def main():
    budget = float(input("Enter how much money you have budgeted this month: "))
    total_spent = 0.0
    while True:
        expense = float(input("Enter an expense or type 0 to stop: "))
        if expense == 0:
            break
        total_spent += expense
    difference = budget - total_spent 
    print("Budget:", budget, "dollars")
    print("Total money spent:", total_spent, "dollars")
    if difference > 0:
        print("You are under budget by", difference, "dollars")
    elif difference < 0:
        print("You are over budget by:", abs(difference), "dollars")
    else:
        print("You spent your exact budget.")



if __name__ == '__main__':
    main()