"""Capital Quiz
Randomly quizzes the user on U.S. state capitals and keeps score.
"""

import random

STATE_CAPITALS = {
    "Alabama": "Montgomery",
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
    "Arkansas": "Little Rock",
    "California": "Sacramento",
    "Colorado": "Denver",
    "Connecticut": "Hartford",
    "Delaware": "Dover",
    "Florida": "Tallahassee",
    "Georgia": "Atlanta",
    "Hawaii": "Honolulu",
    "Idaho": "Boise",
    "Illinois": "Springfield",
    "Indiana": "Indianapolis",
    "Iowa": "Des Moines",
    "Kansas": "Topeka",
    "Kentucky": "Frankfort",
    "Louisiana": "Baton Rouge",
    "Maine": "Augusta",
    "Maryland": "Annapolis",
    "Massachusetts": "Boston",
    "Michigan": "Lansing",
    "Minnesota": "Saint Paul",
    "Mississippi": "Jackson",
    "Missouri": "Jefferson City",
    "Montana": "Helena",
    "Nebraska": "Lincoln",
    "Nevada": "Carson City",
    "New Hampshire": "Concord",
    "New Jersey": "Trenton",
    "New Mexico": "Santa Fe",
    "New York": "Albany",
    "North Carolina": "Raleigh",
    "North Dakota": "Bismarck",
    "Ohio": "Columbus",
    "Oklahoma": "Oklahoma City",
    "Oregon": "Salem",
    "Pennsylvania": "Harrisburg",
    "Rhode Island": "Providence",
    "South Carolina": "Columbia",
    "South Dakota": "Pierre",
    "Tennessee": "Nashville",
    "Texas": "Austin",
    "Utah": "Salt Lake City",
    "Vermont": "Montpelier",
    "Virginia": "Richmond",
    "Washington": "Olympia",
    "West Virginia": "Charleston",
    "Wisconsin": "Madison",
    "Wyoming": "Cheyenne",
}


def main():
    correct = 0
    incorrect = 0

    print("Welcome to the U.S. State Capital Quiz!")
    print("Type the capital of each state. Type 'quit' to stop.\n")

    # Shuffle the states so each one is asked once, in random order
    states = list(STATE_CAPITALS.keys())
    random.shuffle(states)

    for state in states:
        answer = input(f"What is the capital of {state}? ").strip()

        if answer.lower() == "quit":
            break

        actual = STATE_CAPITALS[state]
        # Accept "St. Paul" as well as "Saint Paul"
        if answer.lower().replace("st.", "saint") == actual.lower():
            print("Correct!\n")
            correct += 1
        else:
            print(f"Incorrect. The capital of {state} is {actual}.\n")
            incorrect += 1

    print("--- Quiz Results ---")
    print(f"Correct answers:   {correct}")
    print(f"Incorrect answers: {incorrect}")


if __name__ == "__main__":
    main()