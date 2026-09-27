# Program_2 -- Average Rainfall
# Uses nested loops to collect monthly rainfall data over several years
# and calculate the average rainfall per month.

num_years = int(input("Enter the number of years: "))

total_rainfall = 0.0
total_months = 0

for year in range(1, num_years + 1):
    print(f"\nYear {year}:")
    for month in range(1, 13):
        rainfall = float(input(f"  Enter the inches of rainfall for month {month}: "))
        total_rainfall += rainfall
        total_months += 1

average_rainfall = total_rainfall / total_months

print(f"\nNumber of months: {total_months}")
print(f"Total inches of rainfall: {total_rainfall:.2f}")
print(f"Average rainfall per month: {average_rainfall:.2f} inches")