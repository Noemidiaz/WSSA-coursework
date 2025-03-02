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
draw_url = f"https://deckofcardsapi.com/api/deck/7pah8qz5gpgm/draw/?count=5"
response = requests.get(draw_url)
cards = response.json()["cards"]

# Step 4: Print the value and suit of each card
print("Your 5 Cards:")
for card in cards:
    print(f"{card['value']} of {card['suit']}")


