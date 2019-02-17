from random import randint


CARD_DECK = [['Ace of Spades', 'King of Spades',
              'Queen of Spades', 'Jack of Spades',
              '10 of Spades', '9 of Spades',
              '8 of Spades', '7 of Spades',
              '6 of Spades', '5 of Spades',
              '4 of Spades', '3 of Spades',
              '2 of Spades'],
             ['Ace of Diamonds', 'King of Diamonds',
              'Queen of Diamonds', 'Jack of Diamonds',
              '10 of Diamonds', '9 of Diamonds',
              '8 of Diamonds', '7 of Diamonds',
              '6 of Diamonds', '5 of Diamonds',
              '4 of Diamonds', '3 of Diamonds',
              '2 of Diamonds'],
             ['Ace of Clubs', 'King of Clubs',
              'Queen of Clubs', 'Jack of Clubs',
              '10 of Clubs', '9 of Clubs',
              '8 of Clubs', '7 of Clubs',
              '6 of Clubs', '5 of Clubs',
              '4 of Clubs', '3 of Clubs',
              '2 of Clubs'],
             ['Ace of Hearts', 'King of Hearts',
              'Queen of Hearts', 'Jack of Hearts',
              '10 of Hearts', '9 of Hearts',
              '8 of Hearts', '7 of Hearts',
              '6 of Hearts', '5 of Hearts',
              '4 of Hearts', '3 of Hearts',
              '2 of Hearts']]


def draw(num_0f_cards):

    if [] in current_deck:
        return "The Deck is empty"
    return_cards = []

    for i in range(num_0f_cards):
        rand_one = randint(0, len(current_deck)-1)
        rand_two = randint(0, len(current_deck[rand_one])-1)
        return_cards.append(current_deck[rand_one][rand_two])
        current_deck[rand_one].remove(return_cards[i])
        if [] in current_deck:
            current_deck.remove([])
        if [] in current_deck:
            return return_cards

    return return_cards


current_deck = CARD_DECK.copy()

while True:
    user_input = input()

    if user_input == "quit":
        break
    elif user_input == "draw":
        print(draw(int(input("how name cards? "))))
    elif user_input == "new deck":
        current_deck = CARD_DECK.copy()
        print("There is now a new deck!")


