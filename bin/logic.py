import random
import card as deck

#Variables for game
Face_cards = ['King','Queen','Jack']
Card_types = ['Spades', 'Diamonds', 'Hearts', 'Clubs']
Card_numbers = [1,2,3,4,5,6,7,8,9,10]
FaceCard = False
AceCard = False
Player_Hand = []
Dealer_Hand = []
Card = []
HandValue = 0
DealerHandValue = 0
Prob = random.uniform(0,1)
Player_Lost = False

#Functions to be called throughout the game multiple times#

#Input Test for card#
match_going = True
PlayerTurn = True
total_hand_score = 0
dealer_score = 0
def startMatch():
    match_going == True
    deck.draw_card(Player_Hand,"Player")
    deck.draw_card(Player_Hand,"Player")
    deck.draw_card(Dealer_Hand,"Dealer")
    player_score = deck.ScoreCard(Player_Hand)
    d_score = deck.ScoreCard(Dealer_Hand)
    print("Current Dealer Hand \n", Dealer_Hand)
    print("Current Player Hand\n", Player_Hand)
    return player_score, d_score



def endMatch():
	match_going = False
	return match_going

print("Start")
#Bug,

#deck.deal(int(2),Player_Hand)
#deck.deal(int(1),Dealer_Hand)

startMatch()
d_score = deck.ScoreCard(Dealer_Hand)
player_score = deck.ScoreCard(Player_Hand)
print("Dealer's Hand Score:\n", d_score)
print("Player's Hand Score:\n", player_score)
# The hopefully working game loop :)
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
	PlayerTurn = True
	Player_Hand.clear()
	Dealer_Hand.clear()
	Player_Hand = []
	Dealer_Hand = []
	player_score = 0
	dealer_score = 0
	startMatch() #BUG: Hand & Score is resetting AFTER startMatch() is called
	user_continue_match = ""

if user_continue_match == "N":
	quit()
