import random  # Importing the random module to allow the computer to make a random choice

"""
1 : rock
0 : paper
-1 : scissor
"""

# Computer randomly selects one of the three options
computer = random.choice([1, 0, -1])

# Prompt the user to enter their choice: 'r' for rock, 'p' for paper, 's' for scissor
youstr = input("enter your choice (r for rock, p for paper, s for scissor): ")

# Dictionary to convert user input into corresponding numeric value
your_dict = {"r": 1, "p": 0, "s": -1}

# Dictionary to convert numeric values back to string for display
reverse_dict = {1: "rock", 0: "paper", -1: "scissor"}

# Convert the user's input string to its numeric representation
you = your_dict[youstr]

# Display both choices
print(f"your choice is: {reverse_dict[you]}\ncomputer choice is: {reverse_dict[computer]}")

# Determine the result of the game
if computer == you:
    print("match draw")  # Both choices are the same
else:
    # Logic to determine if the user loses
    # You lose if computer beats your choice (e.g., rock beats scissor, paper beats rock, scissor beats paper)
    if (computer - you == -1) or (computer - you == 2):
        print("you lose")
    else:
        print("you win")  # Otherwise, you win


