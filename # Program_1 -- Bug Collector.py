# Program_1 -- Bug Collector
# Keeps a running total of bugs collected over five days.

total_bugs = 0

for day in range(1, 6):
    bugs = int(input(f"Enter the number of bugs collected on day {day}: "))
    total_bugs += bugs

print(f"\nTotal number of bugs collected over 5 days: {total_bugs}")