import random
#import pygame 

#pygame variables
#pygame.init()
#pscreen = pygame.display.set_mode((1280,720))
#clock = pygame.time.Clock()
#running = True
#



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

#image loading


#temp_button = pygame.image.load('game_images/button.png')
#

#Functions to be called throughout the game multiple times#

#TODO: MAKE PLAYER ABLE TO WITHDRAWL#
def withdrawl():
    while len(Player_Hand) != 0:
	    Player_Hand.pop()

#TODO: MAKE DEALING WORK#
def deal():


	if len(Player_Hand) <= 0:
		draw_card()
	else:
		return
	


	while len(Dealer_Hand) != 5: 
		if len(Dealer_Hand) <= 0:
			dealer_draw_card()
		else:
			return

#TODO: Draw cards on screen when draw button is clicked#
def draw_card(): #some type of variable to put card into dealer or player#
	FaceCard = False
	drawn_card = []
	drawn_type  = round(random.uniform(0,3))
	if drawn_type == 0:
		drawn_type = "Spade"
	if drawn_type == 1:
		drawn_type = "Diamonds"
	if drawn_type == 2:
		drawn_type = "Hearts"
	if drawn_type == 3:
		drawn_type = "Clubs"
		
	Prob = random.uniform(0,1)
	if Prob <= 0.23:
		drawn_number = ""
		drawn_card.append(drawn_type)
		drawn_face  = round(random.uniform(1,3))
		if drawn_face == 1: 
			drawn_face = Face_cards[0]
		if drawn_face == 2:
			drawn_face = Face_cards[1]
		if drawn_face == 3:
			drawn_face = Face_cards[2]
				 
		drawn_face = str(drawn_face)
		drawn_card = drawn_face + " of " + drawn_type
		Player_Hand.append(drawn_card)		

	if Prob > 0.23:
		drawn_number = Card_numbers[round(random.uniform(1,9))]
		drawn_face = ""
		drawn_number = str(drawn_number)
		drawn_card = drawn_number + " of " + drawn_type
		#drawn_card.append(drawn_number)
		#drawn_card.append(drawn_type)
		Player_Hand.append(drawn_card)
	print(drawn_card)
	return(drawn_card,drawn_number,drawn_face)

def dealer_draw_card(): #TODO: CREATE DEALER#
	FaceCard = False
	drawn_card = []
	drawn_number = round(random.uniform(1,10))
	drawn_type  = round(random.uniform(0,3))
	if drawn_number == 1:
		AceCard = True
		drawn_card.append('Ace')
	if drawn_type == 0:
		drawn_type = "Spade"
	if drawn_type == 1:
		drawn_type = "Diamond"
	if drawn_type == 2:
		drawn_type = "Hearts"
	if drawn_type == 3:
		drawn_type = "Clubs"

	if Prob == 0.23:
		FaceCard = True
		drawn_card.append(drawn_type)
	else: 
		drawn_card.append("Dealer Card")
		drawn_card.append(drawn_number)
		drawn_card.append(drawn_type)
		return print(drawn_card)
		Dealer_Hand = [drawn_card]
	print(drawn_card)	
	return

#TODO: CREATE DRAW SYSTEM, UTILIZE Player_Hand.append(draw_card())#
player_hit = False
#Drawing Tests
def ScoreCard(): #Current bug only prints the value of 10 or 20 for some reason, never the actual value of the card.
	for card in range(len(Player_Hand)):
		current_card = Player_Hand[card]
		#if statement hell.
		if current_card == "Ace of Hearts":
			cardscore = 11
		if current_card == "1 of Hearts":
			cardscore = 1
		if current_card == "2 of Hearts":
			cardscore = 2	
		if current_card == "3 of Hearts":
			cardscore = 3
		if current_card == "4 of Hearts":
			cardscore = 4
		if current_card == "5 of Hearts":
			cardscore = 5
		if current_card == "6 of Hearts":
			cardscore = 6
		if current_card == "7 of Hearts":
			cardscore = 7
		if current_card == "8 of Hearts":
			cardscore = 8
		if current_card == "9 of Hearts":
			cardscore = 9
		if current_card == "10 of Hearts":
			cardscore = 10
		if current_card == "King of Hearts" or "Queen of Hearts" or "Jack of Hearts":
			cardscore = 10
		#All Hearts above this#
		if current_card == "Ace of Diamonds":
			cardscore = 11
		if current_card == "1 of Diamonds":
			cardscore = 1
		if current_card == "2 of Diamonds":
			cardscore = 2	
		if current_card == "3 of Diamonds":
			cardscore = 3
		if current_card == "4 of Diamonds":
			cardscore = 4
		if current_card == "5 of Diamonds":
			cardscore = 5
		if current_card == "6 of Diamonds":
			cardscore = 6
		if current_card == "7 of Diamonds":
			cardscore = 7
		if current_card == "8 of Diamonds":
			cardscore = 8
		if current_card == "9 of Diamonds":
			cardscore = 9
		if current_card == "10 of Diamonds":
			cardscore = 10
		if current_card == "King of Diamonds" or "Queen of Diamonds" or "Jack of Diamonds":
			cardscore = 10
		#Diamonds above this#
		if current_card == "Ace of Spades":
			cardscore = 11
		if current_card == "1 of Spades":
			cardscore = 1
		if current_card == "2 of Spades":
			cardscore = 2	
		if current_card == "3 of Spades":
			cardscore = 3
		if current_card == "4 of Spades":
			cardscore = 4
		if current_card == "5 of Spades":
			cardscore = 5
		if current_card == "6 of Spades":
			cardscore = 6
		if current_card == "7 of Spades":
			cardscore = 7
		if current_card == "8 of Spades":
			cardscore = 8
		if current_card == "9 of Spades":
			cardscore = 9
		if current_card == "10 of Spades":
			cardscore = 10
		if current_card == "King of Spades" or "Queen of Spades" or "Jack of Spades":
			cardscore = 10
		#Spades above this#
		if current_card == "Ace of Clubs":
			cardscore = 11
		if current_card == "1 of Clubs":
			cardscore = 1
		if current_card == "2 of Clubs":
			cardscore = 2	
		if current_card == "3 of Clubs":
			cardscore = 3
		if current_card == "4 of Clubs":
			cardscore = 4
		if current_card == "5 of Clubs":
			cardscore = 5
		if current_card == "6 of Clubs":
			cardscore = 6
		if current_card == "7 of Clubs":
			cardscore = 7
		if current_card == "8 of Clubs":
			cardscore = 8
		if current_card == "9 of Clubs":
			cardscore = 9
		if current_card == "10 of Clubs":
			cardscore = 10
		if current_card == "King of Clubs" or "Queen of Clubs" or "Jack of Clubs":
			cardscore = 10
		#Clubs and thats it of if statement hell!#
	total_card_scores = []
	total_card_scores.append(cardscore)
	print(total_card_scores)


	#return(TotalHandScore)

#Player Hit System
player_hit = False
DealerTurn = False

#Choice Handler
def PlayerChoice(action): 
	if action == "Yes" or "Stand" or "Y":
		player_hit = False
		DealerTurn = True
		ScoreCard()
	if action == "No" or "Hit" or "N":
		player_hit = True
		draw_card()
		print("Your Current Hand:\n", Player_Hand)
		ScoreCard()




#Input Tests not offical game#
player_input = input("Draw a number of cards:")
cards_wanted = int(player_input)
for number in range(cards_wanted):
	print("Here is your card")
	draw_card()
	print(Player_Hand)
	print("I am drawing your next card")


while len(Player_Hand) > 0 or DealerTurn == False or Player_Lost == False:
	action_input = str(input("Would you like to stand or hit?"))
	PlayerChoice(action_input)



#


#Assigning Colors to the card





#GAME LOOP#
#while running: 
#	pscreen.fill("purple")
#	print(pygame.mouse.get_pos())
#	#closes game#
#	for event in pygame.event.get():
#		if event.type == pygame.QUIT:
#			running = False
	#			#
#	pygame.display.flip() # think of this as updating the screen with ur work
#	clock.tick(60) # frame limit