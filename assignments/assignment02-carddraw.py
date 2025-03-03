# assignment 02 - card draw
# Description: In the website "Deck of cards API"  https://deckofcardsapi.com/ write a program that shows 5 random cards and the suit of each card.
#By Noemi Diaz



# Step 1: Install the "requests" Library using pip install
import requests

# Step 2: First, shuffle the deck and get the deck_id
shuffle_url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
response = requests.get(shuffle_url)
deck = response.json()
deck_id = deck["deck_id"]

# Step 3: prints out 5 cards
draw_url = f"https://deckofcardsapi.com/api/deck/73r2ibeb8km2/draw/?count=5"
response = requests.get(draw_url)
cards = response.json()["cards"]

# Step 4: Print the value and suit of each card
print("Your 5 Cards:")
for card in cards:
    print(f"{card['value']} of {card['suit']}")



# EXTRA MARKS
# Checking if the user has drawn cards all of the same suit, a pair, triple, straight and congratulate the player for achieving those hands.


# Step 5: Analyze the hand (check for pairs, triples, straight, flush)
values = [card['value'] for card in cards]
suits = [card['suit'] for card in cards]

# Step 6: Count the occurrences of each value and suit
value_counts = {value: values.count(value) for value in values}
suit_counts = {suit: suits.count(suit) for suit in suits}

# Step 7: Check for a flush (all cards same suit)
if max(suit_counts.values()) == 5:
    print("Congrats, you have a flush (all the same suit)!")

# Step 8: Check for a pair and triple
elif 3 in value_counts.values():
    print("Congrats, you have a triple!")
elif 2 in value_counts.values():
    print("Congrats, you have a pair!")


# Step 9: Checking  for a straight (consecutive values)
# Convert face cards to numeric values for comparison
card_value_map = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, 
    "10": 10, "JACK": 11, "QUEEN": 12, "KING": 13, "ACE": 14
}
numeric_values = [card_value_map[card['value']] for card in cards]
numeric_values.sort()

# Checking if the values are consecutive (for straight)
def is_straight(values):
    return all(values[i] + 1 == values[i + 1] for i in range(len(values) - 1))

if is_straight(numeric_values):
    print("Congrats, you have a straight!")


# REFERENCES:
# 