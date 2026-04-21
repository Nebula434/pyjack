import random
import card as deck

#Variables 
Player_Hand = []
Dealer_Hand = []
Card = []
Prob = random.uniform(0,1)

#Functions to be called throughout the game multiple times#
# deck.draw_card((hand you are giving the card to), "Text you want to print out")
# deck.ScoreCard((hand you are scoring aka Dealer_Hand or Player_Hand))
#
#Variables
Player_Hand = []
Dealer_Hand = []
Card = []
Prob = random.uniform(0,1)

#start of game loop, let's set our values
running = True
match_going = True
PlayerTurn = True
total_hand_score = 0
dealer_score = 0
win_streak = 0
def reset(): #NOTE: Purpose of this function is to reset values that need to be used in the next game loop
    Player_Hand.clear()
    Dealer_Hand.clear()
    total_hand_score = 0
    dealer_score = 0
    player_score = 0
    return Player_Hand, Dealer_Hand, total_hand_score, dealer_score, player_score
def start_match():
    match_going = True
    deck.draw_card(Player_Hand,"Player")
    deck.draw_card(Player_Hand,"Player")
    deck.draw_card(Dealer_Hand,"Dealer")
    print("Current Dealer Hand \n", Dealer_Hand)
    print("Current Player Hand\n", Player_Hand)
    return match_going
def end_match():
    match_going = False
    return match_going
print("Start")
start_match()
# The hopefully working game loop :) - This is awesome thank u Dustin :D
while running:
    player_score = deck.ScoreCard(Player_Hand)
    dealer_score = deck.ScoreCard(Dealer_Hand)
    print("Dealer's Hand Score:\n", dealer_score)
    print("Player's Hand Score:\n", player_score)
    while match_going and PlayerTurn: 
        # Grab input inside the loop so it asks every time
        player_input = input("Stand or Hit:\n").lower()

        #check if the player chose to hit
        if player_input == "hit":
            deck.draw_card(Player_Hand,"Player")
            player_score = deck.ScoreCard(Player_Hand)
            print("Player's Hand Score Currently:\n", player_score)

                # Check if they busted after drawing their latest card
            if player_score > 21:
                    print("Past 21! You busted...")
                    PlayerTurn = False
                    match_going = False
                    win_streak = 0

        #Player has chosen to stand, the round is over for them, let the dealer play
        elif player_input == "stand":
            PlayerTurn = False
            print("**Dealer's Turn**") #clarifies dealer is playing
            deck.draw_card(Dealer_Hand,"Dealer") #Dealer has drawn
            dealer_score = deck.ScoreCard(Dealer_Hand) #We score the entire hand again after drawing
            # Dealer must hit until they beat 16
            while dealer_score <= 16:
                deck.draw_card(Dealer_Hand,"Dealer")
                dealer_score = deck.ScoreCard(Dealer_Hand)
                if dealer_score > player_score and dealer_score <= 21: 
                    print("Dealer wins!")
                    match_going = end_match()
                    win_streak = 0
                elif dealer_score > 21:
                    print("Dealer bust you win!")
                    match_going = end_match()
                    win_streak += 1
            if dealer_score < player_score and player_score <= 21:
                print("You win!")
                match_going = end_match()
                win_streak += 1

        elif dealer_score == player_score:
            print("Match was a draw!")
            match_going = end_match() # Ends game loop


    print("Current User Win Streak:",win_streak)
    user_continue_match = input("Continue Playing? Y/N").upper()
    if user_continue_match == "Y":
        reset()
        match_going = True
        PlayerTurn = True
        start_match()
        player_score = deck.ScoreCard(Player_Hand)
        dealer_score = deck.ScoreCard(Dealer_Hand) 
        user_continue_match = ""
        player_input = ""
    else:
        break
