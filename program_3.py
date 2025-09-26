# Program #3: Average Rainfall
# Write a program that uses nested loops to collect data and calculate the average 
# rainfall over a period of years.  
# The program should first ask for the number of years.  
# The outer loop will iterate once for each year. 
# The inner loop will iterate twelve times, once for each month.  
# Each iteration of the inner loop will ask the user for inches of rainfall for each month.  
# After all iterations, the program should display the number of months, 
# the total inches of rainfall, and the average rainfall per month for the entire period.

def main():
    total_rainfall = 0
    total_months = 0
    years = int(input("Enter a number of years: "))
    for year in range(1, years + 1):
        print(f"\nYear {year}:")
        for month in range(1, 13):
            rainfall = float(input("Enter how many inches of rain for this month: "))
            total_rainfall += rainfall
            total_months += 1
    avg_rainfall = total_rainfall / total_months
    print("Total months:", total_months)
    print("Total inches of rain:", total_rainfall)
    print("Avg. rainfall per month:", avg_rainfall)
if __name__ == '__main__':
    main()