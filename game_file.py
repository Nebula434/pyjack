import random
import pygame 
import button

#pygame variables
#pygame.init()
#screen = pygame.display.set_mode((1024,768))
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

#start_img = pygame.image.load('assests/menu/start_button.png').convert_alpha()
#quit_img = pygame.image.load('assests/menu/quit_button.png').convert_alpha()
#settings_img = pygame.image.load('assests/menu/settings_button.png').convert_alpha()
#title_img = pygame.image.load('assests/menu/title_screen.png').convert_alpha()

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
		if drawn_number == 1:
			drawn_number = "Ace"
		drawn_face = ""
		drawn_number = str(drawn_number)
		drawn_card = drawn_number + " of " + drawn_type
		Player_Hand.append(drawn_card)
	#print(drawn_card)
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

Player_Hand_Score = []
Hand_scored = False
def ScoreCard(times_needed): #Current bug only prints the value of 10 or 20 for some reason, never the actual value of the card.
	for card in range(times_needed):
		current_card = str(Player_Hand[card])
		print(current_card)
		#if statement hell.
		if current_card[0:2] == 'Ace of Hearts' or 'Ace of Diamonds' or 'Ace of Clubs' or 'Ace of Spades':
			cardscore = int(11)
		if current_card[0] == '2':
			cardscore = int(2)
		if current_card[0] == '3':
			cardscore = int(3)
			
		if current_card[0] == '4':
			cardscore = int(4)
			
		if current_card[0] == '5':
			cardscore = int(5)
			
		if current_card[0] == '6':
			cardscore = int(6)
			
		if current_card[0] == '7':
			cardscore = int(7)
			
		if current_card[0] == '8':
			cardscore = int(8)
			
		if current_card[0] == '9':
			cardscore = int(9)
		if current_card[0] == '10':
			cardscore = int(10)
			print(current_card, "debug2")

		if current_card[0] == "K" or "Q" or "J":
			cardscore = float(10.0)
			return cardscore
		
		print(cardscore)
		cardscore =+ cardscore

	return cardscore


#Input Test for card#
print("Start")
draw_card()
draw_card()
print(Player_Hand)
ScoreCard(int(len(Player_Hand)))
player_input = str(input("Stand or Hit"))
if player_input == "Hit" :
	draw_card()
	ScoreCard(int(len(Player_Hand)))
	Hand_scored = True
	print(Player_Hand_Score)
if player_input == "Stand":
	#dealer would draw here
	ScoreCard(int(len(Player_Hand)))
	print(Player_Hand_Score)










#Player Hit System
player_hit = False
DealerTurn = False

#Choice Handler
def PlayerChoice(action): 
	if action == "Yes" or "Stand" or "Y":
		player_hit = False
		DealerTurn = True
		return(player_hit)
	if action == "No" or "Hit" or "N":
		player_hit = True
		draw_card()
		print("Your Current Hand:\n", Player_Hand)
		return(player_hit)










#


#Assigning Colors to the card

#classes utilized for game below here
class Menu():
	def __init__(self,x,y, image, scale):
		width = image.get_width()
		height = image.get_height()

		self.image = pygame.transform.scale(image,(int(width * scale),int(height * scale)))
		self.image = image
		self.rect = self.image.get_rect()
		self.rect.topleft = (x,y)
	#def draw(self):
		#screen.blit(self.image,(self.rect.x, self.rect.y))
		

#start_button = button.Button(483, 350, start_img,0.5)
#exit_button = button.Button(483, 425, quit_img,0.5)
#title_screen = Menu(0, -100, title_img, 2)
#player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
#GAME LOOP#
#while running: 


	#print(pygame.mouse.get_pos())
#	screen.fill("white")
#	title_screen.draw()	
#	if start_button.draw(screen) == True:
#		match_start = True
#		print('Start')
#	if exit_button.draw(screen) == True:
#		print("exiting game")
#		running = False
	#closes game#
#	for event in pygame.event.get():
#		if event.type == pygame.QUIT:
#			running = False
	#			#
#	pygame.display.flip() # think of this as updating the screen with ur work
#	clock.tick(60) # frame limit