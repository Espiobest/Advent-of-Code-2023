
with open('data.txt', 'r') as r:
    lines = r.read().splitlines()

def get_rank(hand):
    count = [hand.count(val) for val in hand]
    l = len(set(hand))
    
    if l == 1 and 5 in count:
        return 6
    elif l == 2 and 4 in count and 1 in count:
        return 5
    elif l == 2 and 3 in count and 2 in count:
        return 4
    elif l == 3 and 3 in count and 1 in count:
        return 3
    elif l == 3 and count.count(2) == 4:
        return 2
    elif l == 4 and 2 in count and 1 in count:
        return 1
    else:
        return 0

cards = {v: i for i, v in enumerate('AKQJT98765432')}

hands = []
for line in lines:
    hand, bid = line.split()
    card_rank = get_rank(hand)
    hands.append((hand, int(bid), card_rank))                                              

hands.sort(key=lambda i:([i[2]], [-cards[c] for c in i[0]]))
print("Part 1:", sum(bid * i for i, (_, bid, val) in enumerate(hands, start=1)))

cards = {v: i for i, v in enumerate('AKQT98765432J')}

def get_rank2(hand):
    if 'J' not in hand:
        return get_rank(hand)
    temp_hand = hand.replace('J', '')
    if not temp_hand:
        return get_rank(hand)
    replacement = max(temp_hand, key=hand.count)
    return get_rank(hand.replace('J', replacement))

joker_hands = []
for line in lines:
    hand, bid = line.split()
    card_rank = get_rank2(hand)
    joker_hands.append((hand, int(bid), card_rank))                                              

joker_hands.sort(key=lambda i:([i[2]], [-cards[c] for c in i[0]]))
print("Part 2:", sum(bid * i for i, (_, bid, val) in enumerate(joker_hands, start=1)))
