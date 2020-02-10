import json
import lib

CARD_DB = 'card_database.json'


def load_cards(filename):
    data = json.loads(open(filename).read())
    for cardname in data:
        name = cardname.title()
        cost = data[cardname]['cost']
        effects = data[cardname]['effects']
        atk = data[cardname]['atk']
        defense = data[cardname]['def']
        lib.Card(name, cost, effects, atk, defense)
        print("loading card:",name.upper())

def load_card(cardname):
    global CARD_DB
    data = json.loads(open(CARD_DB).read())
    for name in data:
        if name.lower()==cardname.lower():
            name = cardname.title()
            cost = data[cardname]['cost']
            effects = data[cardname]['effects']
            atk = data[cardname]['atk']
            defense = data[cardname]['def']
            return lib.Card(name, cost, effects, atk, defense)
    return None
        


def search_card(name):
    cards = lib.Card.card_list
    for c in cards:
        if c.name.lower() == name.lower():
            return c
    return None

def load_decks(filename):
    data = json.loads(open(filename).read())
    for deckname in data:
        print(f"\nloading deck: {deckname.upper()}")
        d = lib.Deck(deckname)
        for cardname in data[deckname]:    
            amount = data[deckname][cardname]
            try:
                for i in range(amount):       
                    c = load_card(cardname)
                    d.add_card(c)
                print(f"----  inserted: {c.name} x{amount}")
            except:
                print(f"---- not found: {cardname}")
        print(f"cards: {[str(v) for v in d.cards]}")




