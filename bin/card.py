import random
Face_cards = ['King','Queen','Jack']
Card_types = ['Spades', 'Diamonds', 'Hearts', 'Clubs']
Card_numbers = [1,2,3,4,5,6,7,8,9,10]
#TODO: MAKE PLAYER ABLE TO WITHDRAWL#
#def withdrawl():
#    while len(Player_Hand) != 0:
#	    Player_Hand.pop()

#def deal():#TODO: MAKE DEALING WORK# I got you fam -Dustin

#
#	if len(Logic.Player_Hand) <= 0:
#		draw_card()
#	else:
#		return
#	
#
#	while len(Logic.Dealer_Hand) != 5: 
#		if len(Logic.Dealer_Hand) <= 0:
#			dealer_draw_card()
#		else:
#			return


def draw_card(): #some type of variable to put card into dealer or player#
	import logic as Logic
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
		Logic.Player_Hand.append(drawn_card)		

	if Prob > 0.23:
		drawn_number = Card_numbers[round(random.uniform(1,9))]
		if drawn_number == 1:
			drawn_number = "Ace"
		drawn_face = ""
		drawn_number = str(drawn_number)
		drawn_card = drawn_number + " of " + drawn_type
		Logic.Player_Hand.append(drawn_card)
	print("Player has drawn a: \n", drawn_card)

	return(drawn_card)


#DEALER MECHANICS#
def dealer_draw_card(): #TODO: CREATE DEALER#
    import logic as Logic
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
        Logic.Dealer_Hand.append(dealer_drawn_card)		

    if Prob > 0.23:
        dealer_drawn_number = Card_numbers[round(random.uniform(1,9))]
        if dealer_drawn_number == 1:
            dealer_drawn_number = "Ace"
            dealer_drawn_face = ""
        dealer_drawn_number = str(dealer_drawn_number)
        dealer_drawn_card = dealer_drawn_number + " of " + dealer_drawn_type
        Logic.Dealer_Hand.append(dealer_drawn_card)
        print("Dealer Draws a:\n", dealer_drawn_card)
        return(dealer_drawn_card)


#Scoring Mechanics 
current_card = 0
player_score = 0
def ScoreCard():
    import logic as Logic

    #Hours wasted on scoring alone: 8
    Player_Hand_Score = []
    total_hand_score = 0

    for card in range(len(Logic.Player_Hand)):
    #grab the card we are scoring
        current_card = Logic.Player_Hand[card]
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
    return total_hand_score



dealer_score = 0
def Dealer_ScoreCard():
    import logic as Logic

    #Hours wasted on scoring alone: 8
    Hand_Score = []
    total_hand_score = 0

    for card in range(len(Logic.Dealer_Hand)):
    #grab the card we are scoring
        current_card = Logic.Dealer_Hand[card]
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
        print(current_card)
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
    return total_hand_score
