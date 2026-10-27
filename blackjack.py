import random as rd
import time 

######################################################

card_nr = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Q", "J", "K"]
suits = ["of Spades", "of Hearts", "of Clubs", "of Diamonds"]

sleep_timer = 2

deck = {

}

for c in suits:
    deck[c] = list()

for c in card_nr:
    for v in suits:
        deck[v].append(c)

deck_save = deck

######################################################

def random_card(d):
    s = suits[rd.randint(0, len(suits)) - 1]
    card = d[s][rd.randint(0, len(d[s]) - 1)]
    deck[s].remove(card)
    return card, s

def card_value(card, count_list):
    if isinstance(card, int):
        for i, n in enumerate(count_list):
            count_list[i] += card
        return count_list
    else:
        if card == "A":
            aces = list()
            for i, n in enumerate(count_list):
                aces.append(n + 1)
                count_list[i] += 11
            return count_list + aces
        else:
            for i, n in enumerate(count_list):
                count_list[i] += 10
            return count_list

def print_status(dealt_card, target):
    print(f"""-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Dealt Card: {dealt_card}
To: {target}
-------
Player: {player_count} | {player}
Dealer: {dealer_count} | {dealer}""")

def soft_hard(list):
    for n in list:
        if n[0] == "A":
            return True
    return False

######################################################

cont = True

while cont:

    target = "player"
    cont = True
    dealer = list()
    player = list()
    dealer_count = [0]
    player_count = [0]


    print("----------------- Start Game -----------------")

    card = random_card(deck)
    player.append(str(card))
    player_count = card_value(card[0], player_count)
    print_status(card, target)
    # 1st card dealt to player
    time.sleep(sleep_timer)

    target = "dealer"
    card = random_card(deck)
    dealer.append(str(card))
    dealer_count = card_value(card[0], dealer_count)
    print_status(card, target)
    # 2nd card dealt to dealer
    time.sleep(sleep_timer)

    target = "player"
    card = random_card(deck)
    player.append(str(card))
    player_count = card_value(card[0], player_count)
    print_status(card, target)
    # 3rd card dealt to player
    time.sleep(sleep_timer)

    face_down = random_card(deck)
    dealer.append("face down")
    print_status("face down", "dealer")
    # 4th card is face down to dealer

    while True:
        if len(player_count) == 0:
            print("Player Bust")
            break

        hit = input("Hit or Stand: ")
        if hit.lower() in "stand" or min(player_count) > 21:
            break
        elif hit.lower() in "hit":
            card = random_card(deck)
            player.append(str(card))
            player_count = card_value(card[0], player_count)
            print_status(card, target)
            time.sleep(sleep_timer)

        for i, n in enumerate(player_count):
            if n > 21:
                player_count.pop(i)

    if len(player_count) == 0:
        inp = input("Play again? ")
        if inp.lower() in "yyess":
            cont = True
            deck = deck_save
        else:
            break

    else:
        target = "dealer"
        dealer.append(str(face_down))
        dealer_count = card_value(face_down[0], dealer_count)
        dealer.remove("face down")
        print_status(face_down, "face down card for dealer")
        time.sleep(sleep_timer)

        while True:
            if max(dealer_count + [0]) > 17 or len(dealer_count) == 0 or (max(dealer_count + [0]) == 17 and soft_hard(dealer_count)):
                break

            for i, n in enumerate(dealer_count):
                if n > 21:
                    dealer_count.pop(i)

            card = random_card(deck)
            dealer.append(str(card))
            dealer_count = card_value(card[0], dealer_count)
            print_status(card, target)
            time.sleep(sleep_timer)

            for i, n in enumerate(dealer_count):
                if n > 21:
                    dealer_count.pop(i)

        if max(dealer_count + [0]) == max(player_count + [0]):
            print("Tie")
        elif len(dealer_count) == 0:
            print("Dealer Bust")
        elif max(dealer_count + [0]) > max(player_count + [0]):
            print("Game Over")
        elif max(dealer_count + [0]) < max(player_count + [0]):
            print("Victory")

        inp = input("Play again? ")
        if inp.lower() in "yyess":
            cont = True
            deck = deck_save
        else:
            break
