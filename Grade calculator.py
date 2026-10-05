"""
Weighted Grade Calculator
Asks for scores in each category, averages them, applies the category
weights, and prints the final percentage and letter grade.
"""

# Dictionary: category name -> weight (adds up to 1.0)
WEIGHTS = {"Homework": 0.30, "Quizzes": 0.20, "Midterm": 0.20, "Final": 0.30}

# Tuple of (minimum percent, letter), checked from highest to lowest.
# A tuple is used because the grade scale never changes while running.
GRADE_SCALE = ((90, "A"), (80, "B"), (70, "C"), (60, "D"), (0, "F"))


def get_scores(category):
    """Ask for scores until the user types 'done'; return them as a list."""
    scores = []
    print(f"\nEnter your {category} scores (type 'done' when finished):")

    while True:
        entry = input("  Score: ").strip().lower()

        # Only allow 'done' once at least one score has been entered
        if entry == "done" and scores:
            return scores

        # try/except catches bad input like "abc" (raises ValueError)
        try:
            score = float(entry)
        except ValueError:
            print("  Please enter a number (or 'done' after at least one score).")
            continue

        if 0 <= score <= 100:
            scores.append(score)
        else:
            print("  Score must be between 0 and 100.")


def letter_grade(percent):
    """Return the letter grade for a percentage using GRADE_SCALE."""
    for minimum, letter in GRADE_SCALE:
        if percent >= minimum:
            return letter


def main():
    final_percent = 0

    # Loop through each category and add its weighted average to the total
    for category, weight in WEIGHTS.items():
        scores = get_scores(category)
        average = sum(scores) / len(scores)
        print(f"  {category} average: {average:.2f}")
        final_percent += average * weight

    print(f"\nFinal grade: {final_percent:.2f}% ({letter_grade(final_percent)})")


# Only run main() when this file is run directly
if __name__ == "__main__":
    main() 