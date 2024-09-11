import numpy as np


def deal_poker():
    suits = ['♠', '♥', '♣', '♦']
    values = ['2', 'A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3']
    jokers = ['Joker', 'joker']  

    deck = [f'{value}{suit}' for suit in suits for value in values] + jokers

    np.random.shuffle(deck)

    player1 = deck[:17]
    player2 = deck[17:34]
    player3 = deck[34:51]
    bottom_cards = deck[51:]

    return player1, player2, player3, bottom_cards


player1, player2, player3, bottom_cards = deal_poker()

print(f"玩家1的牌: {player1}")
print(f"玩家2的牌: {player2}")
print(f"玩家3的牌: {player3}")
print(f"底牌: {bottom_cards}")
