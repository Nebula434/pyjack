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

#Bug List#
# After 3 iterations, the game loop ceases. Resulting in card's being drawn but not scored
# and not returning to the game loop. Despite match_going & Player_Turn being true.



#Input Test for card#
match_going = True
PlayerTurn = True
total_hand_score = 0
dealer_score = 0
def reset(): #NOTE: Purpose of this function is to reset values that need to be used in the next loop
    Player_Hand.clear()
    Dealer_Hand.clear()
    total_hand_score = 0
    dealer_score = 0
    d_score = 0
    player_score = 0
    return Player_Hand, Dealer_Hand, total_hand_score, dealer_score, d_score, player_score
def startMatch():
    match_going = True
    deck.draw_card(Player_Hand,"Player")
    deck.draw_card(Player_Hand,"Player")
    deck.draw_card(Dealer_Hand,"Dealer")
    print("Current Dealer Hand \n", Dealer_Hand)
    print("Current Player Hand\n", Player_Hand)
    return (match_going)


def endMatch():
    match_going = False
    return match_going
print("Start")
startMatch()
d_score = deck.ScoreCard(Dealer_Hand)
player_score = deck.ScoreCard(Player_Hand)
print("Dealer's Hand Score:\n", d_score)
print("Player's Hand Score:\n", player_score)
# The hopefully working game loop :) - This is awesome thank u Dustin :D
while match_going and PlayerTurn:
    # Grab input inside the loop so it asks every time
    player_input = input("Stand or Hit:\n").lower()

    if player_input == "hit":
        deck.draw_card(Player_Hand,"Player")
        player_score = deck.ScoreCard(Player_Hand)
        print("Player's Hand Score Currently:\n", player_score)

        # Check if they busted
    if player_score > 21:
            print("Past 21! You busted...")
            PlayerTurn = False
            match_going = False


    elif player_input == "stand":
        PlayerTurn = False
        print("**Dealer's Turn**")
        deck.draw_card(Dealer_Hand,"Dealer")
        dealer_score = deck.ScoreCard(Dealer_Hand)
        # Dealer must hit until they beat 16
        while dealer_score <= 16:
            deck.draw_card(Dealer_Hand,"Dealer")
            dealer_score = deck.ScoreCard(Dealer_Hand)
            
            if dealer_score >= player_score and dealer_score <= 21:
                print("Dealer wins!")
                match_going = endMatch()
            elif dealer_score < player_score and player_score <= 21:
                print("You win!")
                match_going = endMatch()
            elif dealer_score > 21:
                print("Dealer bust you win!")
                match_going = endMatch()


if dealer_score == player_score:
        print("Match was a draw!")
        match_going = endMatch() # Ends game loop

user_continue_match = str(input("Continue Playing? Y/N").upper())
if user_continue_match == "Y":
    reset()
    match_going = startMatch()
    PlayerTurn = True
    player_score = deck.ScoreCard(Player_Hand)
    dealer_score = deck.ScoreCard(Dealer_Hand) 
    user_continue_match = ""
    player_input = ""
if user_continue_match == "N":
    print("Your Are Safe To Close Program")
