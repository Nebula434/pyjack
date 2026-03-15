import random


Card_types = ['Spade', 'Diamond', 'Hearts', 'Clubs']
Card_numbers = [1,2,3,4,5,6,7,8,9,10]
FaceCard = False
AceCard = False
Player_Hand = []
Dealer_Hand = []
Card = []
Prob = random.uniform(0,1)

player_input = int(input("Evening how many cards do u wanna draw?"))



def withdrawl():
    Deleted_cards = []
    while len(Player_Hand) != 0:
	    Player_Hand.pop()
def deal():
	if len(Player_Hand) <= 0:
		draw_card()
	else:
		Skip
	while len(Dealer_Hand) != 5: 
		if len(Dealer_Hand) <= 0:
			draw_card()
		else:
			skip
		
def draw_card(): #some type of variable to put card into dealer or player#
	FaceCard = False
	drawn_card = []
	drawn_number = random.uniform(1,10)
	drawn_type  = random.uniform(0,3)
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
		drawn_card.append(drawn_number)
		drawn_card.append(drawn_type)
		return print(drawn_card)
	print(drawn_card)
	




for cards_wanted in range(player_input):
    draw_card()