import random
def roll():
    min_val= 1
    max_val = 6
    roll = random.randint(min_val, max_val) #using the random function, random outputs will generate

    return roll


while True: #this is the checking with the no. of players
    print("input must be an integer")
    players = int(input("Enter the number of players (2 - 4): "))
    if 2 <= players <= 4: #if there are players less than or greater than 2 and 4 the loop will break
        break
    else:
        print("Must be between 2 - 4 players.")
r=int(input("how many rounds you want to play: ")) #this will consider the no of loops of the game.
for _ in range(r): #the game will be played the number of times of the rounds
    player_scores = [0 for _ in range(players)] #this list is going to store the number of players assigned
    for i in range(players):
        print("\nPlayer number", i+1, "turn has just started!")
        print("Your total score is:", player_scores[i], "\n")
        current_score = 0 #the score is intialized to be zero
        while True:
            should_roll = input("Would you like to roll (y)? ") #user input
            if should_roll.lower() != "y":
                break
            value=roll()
            if value == 1: #if 1 comes the next palyer will get chance
                print("You rolled a 1! Turn done!")
                current_score = 0 # the current score will return back to zero
                break
            else:
                current_score += value # the cumulative addition of current score
                print("You rolled a:", value)
                print("Your score is:", current_score)
                player_scores[i] += current_score # the list is updated with the latest score
                print("Your total score is:",player_scores[i])

max_score = max(player_scores) #among the players the max score score is stored in max_score variable
winner = player_scores.index(max_score) # the built-in index function is going to extract
                            # the index postion of the max score and hence return the player number
print("Player number", winning_idx + 1, "is the winner with a score of:", max_score)
