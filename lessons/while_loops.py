"""Demonstrates while loops by finding low value in string"""

cards: str = "67891"

card_idx: int = 0
low_card: int = int(cards[0])
#look at each number USING INDEXES
while card_idx < 5:
    # check if current card is less than low card
    current_card: int = int(cards[card_idx])
    if (current_card < low_card):
        #update the low card to become current card
        low_card = current_card
    card_idx = card_idx + 1
print(low_card)