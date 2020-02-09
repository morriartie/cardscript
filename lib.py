import random

class Table():
    def __init__(self, deck, hand):
        self.deck = deck
        self.hand = hand


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


class Hand():
    def __init__(self, owner):
        self.cards = []
        self.owner = owner

    def add_card(self, card):
        self.cards.append(card)


class Deck():
    deck_list = []
    def __init__(self, owner, cards=[]):
        Deck.deck_list.append(self)
        self.cards = cards
        self.discard = []
        self.owner = owner

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
