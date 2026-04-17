import random
import pygame 
#import card
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

#TODO: MAKE DEALING WORK# I got you fam -Dustin
# def deal():


#	if len(Player_Hand) <= 0:
#		draw_card()
#	else:
#		return
	


#	while len(Dealer_Hand) != 5: 
#		if len(Dealer_Hand) <= 0:
#			dealer_draw_card()
#		else:
#			return

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
	print("Player has drawn a: \n", drawn_card)

	return(drawn_card)


#DEALER MECHANICS#
def dealer_draw_card(): #TODO: CREATE DEALER#
	FaceCard = False
	dealer_drawn_card = []
	dealer_drawn_type  = round(random.uniform(0,3))
	if dealer_drawn_type == 0:
		dealer_drawn_type = "Spade"
	if dealer_drawn_type == 1:
		dealer_drawn_type = "Diamonds"
	if dealer_drawn_type == 2:
		dealer_drawn_type = "Hearts"
	if dealer_drawn_type == 3:
		dealer_drawn_type = "Clubs"
		
	Prob = random.uniform(0,1)
	if Prob <= 0.23:
		dealer_drawn_number = ""
		dealer_drawn_card.append(dealer_drawn_type)
		dealer_drawn_face  = round(random.uniform(1,3))
		if dealer_drawn_face == 1: 
			dealer_drawn_face = Face_cards[0]
		if dealer_drawn_face == 2:
			dealer_drawn_face = Face_cards[1]
		if dealer_drawn_face == 3:
			dealer_drawn_face = Face_cards[2]
		dealer_drawn_face = str(dealer_drawn_face)
		dealer_drawn_card = dealer_drawn_face + " of " + dealer_drawn_type
		Dealer_Hand.append(dealer_drawn_card)		

	if Prob > 0.23:
		dealer_drawn_number = Card_numbers[round(random.uniform(1,9))]
		if dealer_drawn_number == 1:
			dealer_drawn_number = "Ace"
		dealer_drawn_face = ""
		dealer_drawn_number = str(dealer_drawn_number)
		dealer_drawn_card = dealer_drawn_number + " of " + dealer_drawn_type
		Dealer_Hand.append(dealer_drawn_card)
	print("Dealer Draws a:\n", dealer_drawn_card)
	return(dealer_drawn_card)


current_card = 0
player_score = 0
def ScoreCard(): #Current bug only prints the value of 10 or 20 for some reason, never the actual value of the card.
	#Hours wasted on scoring alone: 8
	Player_Hand_Score = []
	total_hand_score = 0

	for card in range(len(Player_Hand)):
		#grab the card we are scoring
		current_card = Player_Hand[card]
		
		#check if string is in current card, then assign value if so.
		if '2' in current_card:
			cardscore = int(2)
		if '3' in current_card:
			cardscore = int(3)
			
		if '4' in current_card:
			cardscore = int(4)
			
		if '5' in current_card:
			cardscore = int(5)
			
		if '6' in current_card:
			cardscore = int(6)
			
		if '7' in current_card:
			cardscore = int(7)
			
		if '8' in current_card:
			cardscore = int(8)
			
		if '9' in current_card:
			cardscore = int(9)

		if '10' in current_card:
			cardscore = int(10)
			print(current_card, "debug2")
		if 'K' in current_card:
			cardscore = int(10)
		if 'Q' in current_card:
			cardscore = int(10)
		if 'J' in current_card:
			cardscore = int(10)
	

		#move cardscore to an existing list, thanks to u/Naive_Programmer_232 on reddit for this trick
		Player_Hand_Score.append(cardscore)
		#add our total score together by utilzing which loop of the variable we are on. 
		total_hand_score += Player_Hand_Score[card]
		#print our total score
		
		#TODO: Bring total_hand_score OUT of function after it has been completed
	print("Player Hand Score:", total_hand_score)
	return total_hand_score

dealer_score = 0
def Dealer_ScoreCard(): #Current bug only prints the value of 10 or 20 for some reason, never the actual value of the card.
	#Hours wasted on scoring alone: 8
	Hand_Score = []
	total_hand_score = 0

	for card in range(len(Dealer_Hand)):
		#grab the card we are scoring
		current_card = Dealer_Hand[card]
		


		#check if string is in current card, then assign value if so.
		if '2' in current_card:
			cardscore = int(2)
		if '3' in current_card:
			cardscore = int(3)
			
		if '4' in current_card:
			cardscore = int(4)
			
		if '5' in current_card:
			cardscore = int(5)
			
		if '6' in current_card:
			cardscore = int(6)
			
		if '7' in current_card:
			cardscore = int(7)
			
		if '8' in current_card:
			cardscore = int(8)
			
		if '9' in current_card:

			cardscore = int(9)

		if '10' in current_card:

			cardscore = int(10)
			print(current_card, "debug2")
		if 'K' in current_card:
			cardscore = int(10)
		if 'Q' in current_card:
			cardscore = int(10)
		if 'J' in current_card:
			cardscore = int(10)

		#move cardscore to an existing list, thanks to u/Naive_Programmer_232 on reddit for this trick
		Hand_Score.append(cardscore)
		#add our total score together by utilzing which loop of the variable we are on. 
		total_hand_score += Hand_Score[card]
		#print our total score
		dealer_score = total_hand_score
	print("Dealer Hand Score:", total_hand_score)
	return dealer_score
		#TODO: Bring dealer_score OUT of function after it has been completed
	


#Input Test for card#
match_going = True
PlayerTurn = True
total_hand_score = 0
dealer_score = 0

print("Start")
# Using the local draw_card() instead of the card.draw_card()
draw_card()
draw_card()
dealer_draw_card()

print("Current Dealer Hand \n", Dealer_Hand)
print("Current Player Hand\n",Player_Hand)

Dealer_ScoreCard()
player_score = ScoreCard()

# The hopefully working game loop :)
while match_going and PlayerTurn:
	# Grab input inside the loop so it asks every time
	player_input = input("Stand or Hit:\n").lower()

	if player_input == "hit":
		draw_card()
		player_score = ScoreCard()
		print("Player's Hand Score Currently:\n", player_score)

		# Check if they busted
		if player_score > 21:
			print("Past 21! You busted...")
			PlayerTurn = False
			match_going = False

	elif player_input == "stand":
		PlayerTurn = False
		print("**Dealer's Turn**")

		dealer_draw_card()
		dealer_score = Dealer_ScoreCard()

		# Dealer must hit until they beat 16
		while dealer_score <= 16:
			dealer_draw_card()
			dealer_score = Dealer_ScoreCard()
			
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
