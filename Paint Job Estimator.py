# Paint Job Estimator

SQ_FT_PER_GALLON = 112
LABOR_HOURS_PER_GALLON = 8
LABOR_RATE = 35.00

wall_space = float(input("Enter the square feet of wall space: "))
paint_price = float(input("Enter the price of paint per gallon: $"))

gallons = wall_space / SQ_FT_PER_GALLON
hours = gallons * LABOR_HOURS_PER_GALLON
paint_cost = gallons * paint_price
labor_cost = hours * LABOR_RATE
total_cost = paint_cost + labor_cost

print(f"Gallons of paint required: {gallons:.2f}")
print(f"Hours of labor required: {hours:.2f}")
print(f"Cost of the paint: ${paint_cost:,.2f}")
print(f"Labor charges: ${labor_cost:,.2f}")
print(f"Total cost of the paint job: ${total_cost:,.2f}")