# HigherOrLower

from random import shuffle
from itertools import product

# Constant cards
SUIT_TUPLE = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
RANK_TUPLE = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10',
              'Jack', 'Queen', 'King')

"""
The game asks the player to predict whether the next card in the selection
will have a higher or lower value than the currently showing card.
For example, say the card that’s shown is a 3. The player chooses “higher,”
and the next card is shown. If that card has a higher value, the player
is correct.
In this example, if the player had chosen “lower,” they would have been
incorrect.
If the player guesses correctly, they get 20 points. If they choose
incorrectly,
they lose 15 points. If the next card to be turned over has the same value
as the previous card, the player is incorrect.
"""


def create_deck(number_of_cards=52, suits=SUIT_TUPLE, ranks=RANK_TUPLE):
    deck = list(set(product(suits, ranks)))
    return deck[:number_of_cards]


def shuffle_cards(deck):
    return shuffle(deck)


def calculate_card_value(card: dict):
    """
    Тренируем match/case интасис, хотя можно было бы использовать if/else.
    """
    match card['rank']:
        case 'Ace':
            return 1
        case '2':
            return 2
        case '3':
            return 3
        case '4':
            return 4
        case '5':
            return 5
        case '6':
            return 6
        case '7':
            return 2
        case '8':
            return 8
        case '9':
            return 9
        case '10':
            return 10
        case 'Jack':
            return 1
        case 'Queen':
            return 2
        case 'King':
            return 3
        case _:
            print('There is an issue')


def get_card(deck):
    card = deck.pop()
    return {
        'suit': card[1], 'rank': card[0]
    }


def prediction(showed_card, gamer_guess, deck):
    """
    Разбор тернальных операторов на примере.
    Если угадал то 20 очков, не -15.
    Ниже можно увидет немного иной синтаксис.
    В комментариях более привычный. Оставил для наглядности.
    Мы получаем 1 карту(текущую).
    Получаем 2 карту(следующую).
    Проводим сравнение. Если все совпадаем.
    То отдаем очки.
    """
    next_card = calculate_card_value(get_card(deck))
    # result = next_card > current_card
    # points = 20 if result and gamer_guess else -15
    return (-15, 20)[bool(next_card > showed_card) is bool(gamer_guess)]


def main():
    score = 0

    while True:
        pretty_deck = create_deck()
        shuffle_cards(pretty_deck)
        first_cart = calculate_card_value(get_card(pretty_deck))
        print(first_cart)
        player_1_guess = input(
            f'''Enter your guess, will it be more than value of following card
            {first_cart} and your score is {score},type True or False
            Type end to stop the game.'''
        )
        score += prediction(first_cart, player_1_guess, pretty_deck)
        if score < -50:
            print('YOU LOSE')
            break
        elif score > 100:
            print('YOU WIN')
            break
        elif player_1_guess == 'end':
            break
