import random as rd

######################################################



card_nr = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Q", "J", "K"]
suits = ["of Spades", "of Hearts", "of Clubs", "of Diamonds"]

sleep_timer = 2

deck = {

}


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

reps = int(input("Repetitions: "))
reps_h = reps
player_Hit = int(input("Player hits before (not included): "))
player_Victories = 0
dealer_Victories = 0

while reps > 0:

    dealer = list()
    player = list()
    dealer_count = [0]
    player_count = [0]
    reps -= 1

    deck = {

    }

    for c in suits:
        deck[c] = list()

    for c in card_nr:
        for v in suits:
            deck[v].append(c)


    print("----------------- Start Game -----------------")
    card = random_card(deck)
    player.append(str(card))
    player_count = card_value(card[0], player_count)
    # 1st card dealt to player

    card = random_card(deck)
    dealer.append(str(card))
    dealer_count = card_value(card[0], dealer_count)
    # 2nd card dealt to dealer

    card = random_card(deck)
    player.append(str(card))
    player_count = card_value(card[0], player_count)
    # 3rd card dealt to player

    face_down = random_card(deck)
    dealer.append("face down")
    # 4th card is face down to dealer

    while True:
        if len(player_count) == 0:
            print("Player Bust")
            break

        if not max(player_count + [0]) < player_Hit:
            break

        else:
            card = random_card(deck)
            player.append(str(card))
            player_count = card_value(card[0], player_count)

        for i, n in enumerate(player_count):
            if n > 21:
                player_count.pop(i)

    if len(player_count) == 0:
        dealer_Victories += 1

    else:
        dealer.append(str(face_down))
        dealer_count = card_value(face_down[0], dealer_count)
        dealer.remove("face down")

        while True:
            if max(dealer_count + [0]) > 17 or len(dealer_count) == 0 or (max(dealer_count + [0]) == 17 and soft_hard(dealer)):
                break

            for i, n in enumerate(dealer_count):
                if n > 21:
                    dealer_count.pop(i)

            card = random_card(deck)
            dealer.append(str(card))
            dealer_count = card_value(card[0], dealer_count)

            for i, n in enumerate(dealer_count):
                if n > 21:
                    dealer_count.pop(i)

        if max(dealer_count + [0]) == max(player_count + [0]):
            print("Tie")
        elif len(dealer_count) == 0:
            print("Dealer Bust")
            player_Victories += 1
        elif max(dealer_count + [0]) > max(player_count + [0]):
            print("Game Over")
            dealer_Victories += 1
        elif max(dealer_count + [0]) < max(player_count + [0]):
            print("Victory")
            player_Victories += 1

print(f"""
Player: {player_Victories}
Dealer: {dealer_Victories}
Games: {reps_h}""")
