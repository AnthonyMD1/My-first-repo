# Automobile Costs
# Asks for monthly automobile expenses, then displays the monthly and annual totals.

# Get the monthly cost of each expense
loan = float(input("Enter monthly loan payment: $"))
insurance = float(input("Enter monthly insurance cost: $"))
gas = float(input("Enter monthly gas cost: $"))
oil = float(input("Enter monthly oil cost: $"))
tires = float(input("Enter monthly tires cost: $"))
maintenance = float(input("Enter monthly maintenance cost: $"))

# Calculate totals
monthly_total = loan + insurance + gas + oil + tires + maintenance
annual_total = monthly_total * 12

# Display results
print(f"\nTotal monthly cost: ${monthly_total:,.2f}")
print(f"Total annual cost: ${annual_total:,.2f}")