import math, collections

def is_royal_flush(ranks, suits):
    if is_straight(ranks, suits)[0] and is_flush(ranks, suits)[0] and ranks[0] == 10:
        return True, 10e6
    return False, 0

def is_straight_flush(ranks, suits):
    if is_straight(ranks, suits)[0] and is_flush(ranks, suits)[0]:
        return True, 9e6
    return False, 0

def is_four(ranks, suits):
    x = collections.Counter(ranks).most_common(2)
    if x[0][1] == 4:
        return True, 8e6
    return False, 0

def is_full_house(ranks, suits):
    x = collections.Counter(ranks).most_common(2)
    if x[0][1] == 3 and x[1][1] == 2:
        return True, 7e6 + x[0][0]*15 + x[1][0]
    return False, 0

def is_flush(ranks, suits):
    if suits[0] == suits[1] and suits[0] == suits[2] and suits[0] == suits[3] and suits[0] == suits[4]:
        ranks.sort()
        return True, 6e6 + ranks[4] * 15 ** 4 + ranks[3] * 15 ** 3 + ranks[2] * 15 ** 2 + ranks[1] * 15 * ranks[0]
    return False, 0

def is_straight(ranks, suits):
    x = collections.Counter(ranks).most_common(5)
    if x[0][1]==1 and ranks[4] - ranks[0] == 4:
        return True, 5e6 + ranks[0]
    return False, 0

def is_three(ranks, suits):
    x = collections.Counter(ranks).most_common(5)
    if x[0][1] == 3:
        tmp = [x[1][0], x[2][0]]
        tmp.sort()
        return True, 4e6 + x[0][0] * 15 ** 2 + tmp[1] * 15 + tmp[0]
    return False, 0

def is_two_pair(ranks, suits):
    global value
    x = collections.Counter(ranks).most_common(5)
    if x[0][1] == 2 and x[1][1] == 2:
        tmp = [x[0][0], x[1][0]]
        tmp.sort()
        return True, 3e6 + tmp[1] * 15 ** 2 + tmp[0] * 15 + x[2][0]
    return False, 0


def is_one_pair(ranks, suits):
    global value
    x = collections.Counter(ranks).most_common(5)
    if x[0][1] == 2:
        tmp = [x[1][0], x[2][0], x[3][0]]
        tmp.sort()
        return True, 2e6 + x[0][0] * 15 ** 3 + tmp[2] * 15**2 + tmp[1] * 15 + tmp[0]
    return False, 0


def is_high_card(ranks, suits):
    global value
    x = collections.Counter(ranks).most_common(5)
    if x[0][1] == 1:
        return True, 1e6 + ranks[4] * 15 ** 4 + ranks[3] * 15 ** 3 + ranks[2] * 15 ** 2 + ranks[1] * 15 + ranks[0]
    return False, 0

def hand_to_rankssuits(hand):
    ranks = [
        10 if card[0] == 'T' else 11 if card[0] == 'J' else 12 if card[0] == 'Q' else 13 if card[0] == 'K' else 14 if
        card[0] == 'A' else int(card[0]) for card in hand]
    suits = [card[1] for card in hand]
    return ranks, suits

def eval_hand(hand):
    ranks, suits = hand_to_rankssuits(hand)
    ranks.sort()
    functions = [is_royal_flush, is_straight_flush, is_four, is_full_house, is_flush,
                 is_straight, is_three, is_two_pair, is_one_pair, is_high_card]
    for f in functions:
      [flag, value] = f(ranks, suits)
      if flag:
        break
    return value

f = open('/home/hofmann/pjeuler_python/pjeuler/input/54')
wins = 0
for both_hands in f.readlines():
    hand1 = both_hands.rstrip().split(' ')[:5]
    hand2 = both_hands.rstrip().split(' ')[5:]
    val1 = eval_hand(hand1)
    val2 = eval_hand(hand2)
    if val1 > val2:
        wins += 1
print(wins)