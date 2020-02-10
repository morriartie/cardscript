import random

class Table():
    def __init__(self, deck1, deck2):
        self.deck1 = deck1
        self.deck2 = deck2
        self.current_turn = 0


class Card():
    card_list = []
    def __init__(self, name, cost, effects, atk=None, defense=None):
        Card.card_list.append(self)
        #
        self.name = name
        self.cost = cost
        self.effects = effects
        self.atk = atk
        self.defense = defense

    def __str__(self):
        icons = ''
        if 'fast' in self.effects:
            icons += '='
        if 'fly' in self.effects:
            icons += '&'
        if 'strong' in self.effects:
            icons += '*'
        return f"{self.name.title()}({icons})[{self.atk}/{self.defense}]"


class Hand():
    def __init__(self, owner, deck=None):
        self.cards = []
        self.owner = owner
        self.deck = None

    def buy(self):
        c = self.deck.buy()
        self.cards.append(c)

    def add_card(self, card):
        self.cards.append(card)


class Deck():
    deck_list = []
    def __init__(self, name, hand=None):
        Deck.deck_list.append(self)
        self.name = name.title()
        self.cards = []
        self.discard = []
        self.hand = hand

    def add_card(self,card):
        self.cards.append(card)

    def buy(self, n):
        bought = self.cards[-n:]
        self.cards = self.cards[:-n]
        return bought

    def shuffle(self):
        random.shuffle(self.cards)

    def get_deck_size(self):
        return len(self.cards)

    def search_deck(deckname):
        result = [v for v in Deck.deck_list if v.name.lower()==deckname.lower()]
        if result:
            return result[0]
        else:
            return None
