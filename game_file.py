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

current_card = 0
player_score = 0
def ScoreCard(): #Current bug only prints the value of 10 or 20 for some reason, never the actual value of the card.
	Player_Hand_Score = []
	total_hand_score = 0

	for card in range(len(Player_Hand)):
		#grab the card we are scoring
		current_card = Player_Hand[card]
		

		
		print("next card is being scored here")
		print("Current Card Being Scored\n", current_card)


		#check if string is in current card, then assign value if so.
		if '2' in current_card:
			print("this has been ran and the score should be 2")
			cardscore = int(2)
		if '3' in current_card:
			print("this has been ran and the score should be 3")
			cardscore = int(3)
			
		if '4' in current_card:
			print("this has been ran and the score should be 4")
			cardscore = int(4)
			
		if '5' in current_card:
			print("this has been ran and the score should be 5")
			cardscore = int(5)
			
		if '6' in current_card:
			print("this has been ran and the score should be 6")
			cardscore = int(6)
			
		if '7' in current_card:
			print("this has been ran and the score should be 7")
			cardscore = int(7)
			
		if '8' in current_card:
			print("this has been ran and the score should be 8")
			cardscore = int(8)
			
		if '9' in current_card:
			print("this has been ran and the score should be 9")
			cardscore = int(9)

		if '10' in current_card:
			print("this has been ran and the score should be 10")
			cardscore = int(10)
			print(current_card, "debug2")
		if 'K' in current_card:
			cardscore = int(10)
		if 'Q' in current_card:
			cardscore = int(10)
		if 'J' in current_card:
			cardscore = int(10)
	
		#check if card score is actually a value other than 10 or 20, see github for why
		print(cardscore, ": Supposed to be cardscore after running through all if statements.")


		#move cardscore to an existing list, thanks to u/Naive_Programmer_232 on reddit for this trick
		Player_Hand_Score.append(cardscore)
		print(Player_Hand_Score, ":Total Player Hand Score")
		#add our total score together by utilzing which loop of the variable we are on. 
		total_hand_score += Player_Hand_Score[card]
		#print our total score
		print("Current Hand Score:", total_hand_score)
		player_score = total_hand_score
		print(player_score)
		#return our score back.

#Input Test for card#
print("Start")
draw_card()
draw_card()
print("Current Player Hand\n", Player_Hand)
print(len(Player_Hand), "Length of Player Hand")
ScoreCard()
while player_score < 21:
	player_input = str(input("Stand or Hit"))
	if player_input == "Hit" or "hit":
		draw_card()
		total_hand_score = ScoreCard()
		print(total_hand_score)
		Hand_scored = True
	if player_input == "Stand" or "stand":
		#dealer would draw here
		total_hand_score = ScoreCard()
		print(total_hand_score)





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
#	clock.tick(60) # frame limitre
