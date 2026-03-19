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
Card_types = ['Spade', 'Diamond', 'Hearts', 'Clubs']
Card_numbers = [1,2,3,4,5,6,7,8,9,10]
FaceCard = False
AceCard = False
Player_Hand = []
Dealer_Hand = []
Card = []
HandValue = 0
DealerHandValue = 0
Prob = random.uniform(0,1)


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
		drawn_type = "Diamond"
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

#Drawing Tests
player_input = input("Draw a number of cards:")
cards_wanted = int(player_input)
for number in range(cards_wanted):
	print("Here is your card")
	draw_card()
	print(Player_Hand)
	print("I am drawing your next card")
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