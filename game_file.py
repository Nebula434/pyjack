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
    while len(Player_Hand) != 0:
	    Player_Hand.pop()

# game logic need to touch this up before implementing #
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


def draw_card(drawn_card): #some type of variable to put card into dealer or player#
	FaceCard = False
	drawn_card = []
	drawn_number = round(random.uniform(1,10))
	drawn_type  = round(random.uniform(0,3))
	if drawn_type == 0:
		drawn_type = "Spade"
	if drawn_type == 1:
		drawn_type = "Diamond"
	if drawn_type == 2:
		drawn_type = "Hearts"
	if drawn_type == 3:
		drawn_type = "Clubs"

	if drawn_number == 1:
		AceCard = True
		drawn_card.append('Ace')

	if Prob <= 0.23:
		FaceCard = True
		drawn_card.append(drawn_type)
	else: 
		drawn_card.append(drawn_number)
		drawn_card.append(drawn_type)
		Player_Hand.append(drawn_card)
		return drawn_card 
	print(drawn_card)

def dealer_draw_card(): #seperate function for creating dealer cards#
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


# testing player draw #
for cards_wanted in range(player_input):
    draw_card()

	
# 					  #

#testing dealer logic#
while len(Dealer_Hand) != 0 and len(Dealer_Hand) == 5:
	dealer_draw_card()
