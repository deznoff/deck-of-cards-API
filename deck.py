import requests
import json

class CardGame:
    def __init__(self):
        deck_response = requests.get('https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1')
        self.deck_body = json.loads(deck_response.content)
    
    #Create a method to get a Deck ID
    def get_deck_id(self):
        return self.deck_body['deck_id']

    def return_drawn_card(self):
        draw_count = input('Type in the number of cards to draw: ')
        payload = {'count': draw_count}
        return json.loads(requests.get(f'https://deckofcardsapi.com/api/deck/{self.get_deck_id()}/draw', 
                                       params=payload).content)
    


card_game1 = CardGame()
print(card_game1.return_drawn_card())

#draw_cnt = input('Type in a number of cards to draw: ')
