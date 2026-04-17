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

print("Start")
# Using the local draw_card() instead of the card.draw_card()
deck.draw_card()
deck.draw_card()
deck.dealer_draw_card()

print("Current Dealer Hand \n", Dealer_Hand)
print("Current Player Hand\n",Player_Hand)

deck.Dealer_ScoreCard()
player_score = deck.ScoreCard()

# The hopefully working game loop :)
while match_going and PlayerTurn:
	# Grab input inside the loop so it asks every time
	player_input = input("Stand or Hit:\n").lower()

	if player_input == "hit":
		deck.draw_card()
		player_score = deck.ScoreCard()
		print("Player's Hand Score Currently:\n", player_score)

		# Check if they busted
		if player_score > 21:
			print("Past 21! You busted...")
			PlayerTurn = False
			match_going = False

	elif player_input == "stand":
		PlayerTurn = False
		print("**Dealer's Turn**")

		deck.dealer_draw_card()
		dealer_score = deck.Dealer_ScoreCard()

		# Dealer must hit until they beat 16
		while dealer_score <= 16:
			deck.dealer_draw_card()
			dealer_score = deck.Dealer_ScoreCard()
			
			if dealer_score >= player_score and dealer_score <= 21:
				print("Dealer wins!")
			elif dealer_score < player_score and player_score <= 21:
				print("You win!")
			elif dealer_score > 21:
				print("Dealer bust you win!")
if dealer_score == player_score:
		print("Match was a draw!")

		match_going = False # Ends game loop
input("Press enter to continue")
