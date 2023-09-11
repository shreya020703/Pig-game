import random


def roll():
    min_val= 1
    max_val = 6
    roll = random.randint(min_val, max_val)

    return roll


while True:
    print("input must be an integer")
    players = int(input("Enter the number of players (2 - 4): "))
    if 2 <= players <= 4:
        break
    else:
        print("Must be between 2 - 4 players.")
r=int(input("how many rounds you want to play"))
for _ in range(r):
    player_scores = [0 for _ in range(players)]
    for i in range(players):
        print("\nPlayer number", i+1, "turn has just started!")
        print("Your total score is:", player_scores[i], "\n")
        current_score = 0
        while True:
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != "y":
                break
            value=roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a:", value)
                print("Your score is:", current_score)
                player_scores[i] += current_score
                print("Your total score is:",player_scores[i])

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("Player number", winning_idx + 1, "is the winner with a score of:", max_score)
