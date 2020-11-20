from collections import Counter
import math

value = 0


def is_royal_flush(ranks, suits):
    global value
    if is_straight(ranks) and is_flush(ranks, suits) and ranks[0] == 10:
        value = 10e6
        return True
    return 0


def is_straight_flush(ranks, suits):
    global value
    if is_straight(ranks) and is_flush(ranks, suits):
        value = 9e6
        return True
    return 0


def is_four(ranks):
    global value
    x = Counter(ranks).most_common(2)
    if x[0][1] == 4:
        value = 8e6
        return True
    return False


def is_full_house(ranks):
    global value
    x = Counter(ranks).most_common(2)
    if x[0][1] == 3 and x[1][1] == 2:
        value = 7e6 + x[0][0]*15 + x[1][0]
        return True
    return False


def is_flush(ranks, suits):
    global value
    if suits[0] == suits[1] and suits[0] == suits[2] and suits[0] == suits[3] and suits[0] == suits[4]:
        ranks.sort()
        value = 6e6 + ranks[4] * 15 ** 4 + ranks[3] * 15 ** 3 + ranks[2] * 15 ** 2 + ranks[1] * 15 * ranks[0]
        return True
    return False


def is_straight(ranks):
    global value
    x = Counter(ranks).most_common(5)
    if x[0][1]==1 and ranks[4] - ranks[0] == 4:
        value = 5e6 + ranks[0]
        return True


def is_three(ranks):
    global value
    x = Counter(ranks).most_common(5)
    if x[0][1] == 3:
        tmp = [x[1][0], x[2][0]]
        tmp.sort()
        value = 4e6 + x[0][0] * 15 ** 2 + tmp[1] * 15 + tmp[0]
        return True


def is_two_pair(ranks):
    global value
    x = Counter(ranks).most_common(5)
    if x[0][1] == 2 and x[1][1] == 2:
        tmp = [x[0][0], x[1][0]]
        tmp.sort()
        value = 3e6 + tmp[1] * 15 ** 2 + tmp[0] * 15 + x[2][0]
        return True


def is_one_pair(ranks):
    global value
    x = Counter(ranks).most_common(5)
    if x[0][1] == 2:
        tmp = [x[1][0], x[2][0], x[3][0]]
        tmp.sort()
        value = 2e6 + x[0][0] * 15 ** 3 + tmp[2] * 15**2 + tmp[1] * 15 + tmp[0]
        return True


def is_high_card(ranks):
    global value
    x = Counter(ranks).most_common(5)
    if x[0][1] == 1:
        value = 1e6 + ranks[4] * 15 ** 4 + ranks[3] * 15 ** 3 + ranks[2] * 15 ** 2 + ranks[1] * 15 + ranks[0]
        return True


def hand_to_rankssuits(hand):
    ranks = [
        10 if card[0] == 'T' else 11 if card[0] == 'J' else 12 if card[0] == 'Q' else 13 if card[0] == 'K' else 14 if
        card[0] == 'A' else int(card[0]) for card in hand]
    suits = [card[1] for card in hand]
    return ranks, suits


def eval_hand(hand):
    ranks, suits = hand_to_rankssuits(hand)
    ranks.sort()
    if is_royal_flush(ranks, suits):
        1 + 1
    elif is_straight_flush(ranks, suits):
        1 + 1
    elif is_four(ranks):
        1 + 1
    elif is_full_house(ranks):
        1 + 1
    elif is_flush(ranks, suits):
        1 + 1
    elif is_straight(ranks):
        1 + 1
    elif is_three(ranks):
        1 + 1
    elif is_two_pair(ranks):
        1 + 1
    elif is_one_pair(ranks):
        1 + 1
    elif is_high_card(ranks):
        1 + 1
    else:
        print('what?')
        quit()
    return value


f = open('p054_poker.txt', 'r')
wins1 = 0
counter = 0
for both_hands in f.readlines():

    hand1 = both_hands.rstrip().split(' ')[:5]
    hand2 = both_hands.rstrip().split(' ')[5:]

    value = 0
    val1 = eval_hand(hand1)

    value = 0
    val2 = eval_hand(hand2)

    if math.floor(val1*1e-6) == 5 or 5 == math.floor(val2*1e-6):
        print(hand1, hand2)
        print(val1, val2)

    if val1 > val2:
        wins1 += 1
print(wins1)
