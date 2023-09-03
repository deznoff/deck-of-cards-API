import requests
import json

class CardGame:
    deck_response = requests.get('https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1')
    deck_body = json.loads(deck_response.content)
    deck_id = deck_body['deck_id']

card_game1 = CardGame()


draw_cnt = input('Type in a number of cards to draw: ')

print(deck_id)