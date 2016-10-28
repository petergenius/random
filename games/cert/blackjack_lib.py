import skilstak.colors as c
from time import sleep


def create_cards():
    suits = ['diamonds', 'clubs', 'hearts', 'spades']
    values = [['ace', 11], ['jack', 10], ['queen', 10], ['king', 10], ['2', 2], ['3', 3], ['4', 4], ['5', 5], ['6', 6], ['7', 7], ['8', 8], ['9', 9], ['10', 10]]
    standardDeck = []
    for cardList in values:
        for suit in suits:
            word = cardList[0] + " of " + suit
            value = cardList[1]
            minilist = [word, value]
            standardDeck.append(minilist)
    return standardDeck


def print_rules():
    print('''
{}Objective{}:Get as close to 21 points without going over.
{}How to win{}:Be the closest to 21 points. If you go over, you lose.
{}Point values{}:All cards are worth the value on the card, and face cards are worth 10.
{}Aces{}:Aces can be used as 1 or 11 points.
'''.format(c.y, c.x, c.y, c.x, c.y, c.x, c.y, c.x))
    input('Press enter to continue.\n')


def knows_how_to_play():
    answered = False
    while answered is False:
        answer = input('{}{}Does everyone know how to play blackjack?({}Y{}/{}n{}) > {}'.format(c.x, c.cl, c.g, c.x, c.r, c.x, c.c)).lower().strip()
        if 'y' in answer:
            answered = True
        elif 'n' in answer:
            answered = True
            printrules()
        else:
            print('{}Invalid. Please say {}yes{} or {}no{}.'.format(c.x, c.g, c.x, c.r, c.x))


def isAce(card):
    if 'ace' in card:
        return True
    return False


def hasAce(aces):
    hasAce = False
    for ace in aces:
        if ace == 11:
            aces.remove(11)
            aces.append(1)
            hasAce = True
            break
    return hasAce, aces


def get_two_cards(deck):
    card = deck.pop()
    card2 = deck.pop()
    if isAce(card[0]) and isAce(card2[0]):
        total = 12
    else:
        total = card[1] + card2[1]
    titleOne = card[0]
    titleTwo = card2[0]
    return titleOne, titleTwo, total, deck


def get_players():
    try:
        while True:
            players = input('How many players? > ' + c.c)
            if players.isdigit():
                return int(players)
            else:
                print('{}Please type a {}number{}.'.format(c.x, c.r, c.x))
    except KeyboardInterrupt:
        print(c.cl)
        exit()

def print_hand(titleOne, titleTwo, total):
    print('Your hand contains the {}{}{}  and the {}{}{} for a total of {}{}{} points.'.format(c.b, titleOne, c.x, c.b, titleTwo, c.x, c.m, total, c.x))


def get_one_more_card(deck, total):
    card = deck.pop()
    title = card[0]
    total += card[1]
    print(c.x+'{}Your new card is the {}{}{}. You now have {}{}{} Points.'.format(c.b, title, c.x, c.m, total, c.x))
    return total, deck, title


def ask_to_hit(hand, firstTime):
    try:
        while True:
            itemstring = 'Your hand contains:'
            for item in hand:
                itemstring += item + ' '
            if firstTime is False:
                print(itemstring)
            wantToHit = input('Would you like to hit (take another card)? > ' + c.c).strip().lower()
            if 'y' in wantToHit:
                return True
                break
            elif 'n' in wantToHit:
                return False
                break
            else:
                print('{}Please type {}yes{} or {}no{}.'.format(c.x, c.g, c.x, c.r, c.x))
    except KeyboardInterrupt:
        print(c.cl)
        exit()


def get_round_values(players):
    firstTime = []
    hands = []
    totals = []
    aces = []
    for x in range(players):
        firstTime.append(True)
        totals.append(0)
        hands.append([])
        aces.append([])
    return firstTime, hands, totals, aces


def gen_perm_values(players):
    playerNames = []
    losses = []
    wins = []
    ties = []
    for x in range(players):
        playerNames.append('Player '+str(x + 1))
        wins.append(0)
        ties.append(0)
        losses.append(0)
    return playerNames, wins, ties, losses


def find_best(totals, hands):
    highest = 0
    shortest = 999
    for total in totals:
        if total < 22:
            if total > highest:
                highest = total
    for x in range(len(totals)):
        if totals[x] == highest and len(hands[x]) < shortest:
            shortest = len(hands[x])

    return highest, shortest


def find_winners(totals, hands, losses):
    highest, shortest = findBest(totals, hands)
    winners = []
    for x in range(len(totals)):
        if totals[x] == highest and len(hands[x]) == shortest:
            winners.append(x)
        else:
            losses[x] += 1
    return winners, losses


def add_aces(card1, card2, aces):
    if isAce(card1):
        aces.append(11)
    elif isAce(card2):
        aces.append(11)
    return aces


def print_winners(playerNames, winners, wins, ties):
    if len(winners) > 1:
        names = ''
        string = 'The winners are:'
        for name in winners:
            ties[name] += 1
            names += playerNames[name] + ' '
        print(string + c.o+names+c.x)
    elif len(winners) == 1:
        print('{}The winner is {}{}{}!'.format(c.x, c.g, playerNames[winners[0]], c.x))
        wins[winners[0]] += 1
    else:
        print('{}Nobody{} won this round!'.format(c.r,c.x))
    return wins, ties


def print_data(playerNames, wins, ties, losses, stage, hands, totals):
    for i in range(len(playerNames)):
        hand = ""
        for card in hands[i]:
            hand += (card + ", ")
        hand = hand[:-2]
        print("{}{}{} card's include: {}{}{} for a total of: {}{}{} points.".format(c.m, playerNames[i], c.x, c.y, hand, c.x, c.b, totals[i], c.x))
    print('\nplayer  |wins|ties|losses|%win/tie|%lose')
    for x in range(len(playerNames)):
        losspercent = round(losses[x]/(stage+1)*100, 2)
        winpercent = 100 - losspercent
        print('{}|{}   |{}   |{}     |{}    |{}    '.format(playerNames[x], wins[x], ties[x], losses[x], winpercent, losspercent))
    print('\n\n')


def print_intro():
    print('''{}{}Welcome to {}Blackjack{}!
Created by: {}Peter S.{}
Version: {}0.9.5{}'''.format(c.x, c.cl, c.g, c.x, c.b, c.x, c.m, c.x))


def print_starting_data(rounds):
    print('''{}{}
Maximum rounds:{}{}{}
Decks used: {}8{}
{}Note{}: Earlier players are at a disadvantage
if you let other people look at your screen.'''.format(c.cl, c.x, c.y, rounds-1, c.x, c.y, c.x, c.y, c.x))

