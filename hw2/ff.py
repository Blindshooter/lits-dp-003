import sys
import random

def main111():
    game = 1
    cap = 500
    p1score = 0
    p2score = 0
    print 'Welcome'
    while p1score<500 and p2score<500:
        p1, p2 = game()
        p1score+=p1
        p2score+=p2
        game+=1



def main():
    deck = Deck()
    deck.shuffle()
    Hand1 = Hand()
    deck.draw(Hand1, 5)
    Hand2 = Hand()
    deck.draw(Hand2, 5)


    pile = Hand()
    deck.draw(pile,1)
    print "Upper pile card is: %s" % pile.cards[-1]

    hands = [Hand1.cards, Hand2.cards]
    n = 1
    while n>=4:#len(Hand1.cards)>0 and len(Hand2.cards)>0:
        current_player = 0
        print "Player %i turn" %current_player+1
        print "Player %i hand:" % current_player+1
        print hands[current_player]
        print hands[current_player].points_count()
        a1 = int(raw_input('Your action (0 to draw a card): '))
        n-=1
        if a1==0:
            deck.draw(hands[current_player-1],1)
        elif 1<=a1<= hands[current_player]

        #game flow
        pass
    return hands[0].points_count(), hands[1].points_count()



class Card(object):
    colors = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    pts = [15, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 10, 10]
    def __init__(self, color = 0, rank = 0):
        self.color = color
        self.rank = rank

    def __str__(self):
        return '%s of %s' % (Card.ranks[self.rank], Card.colors[self.color])

    def points(self):
        return Card.pts[self.rank]


class Deck(Card):

    def __init__(self):
        self.cards = []
        for color in range(4):
            for rank in range(13):
                card = Card(color, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def shuffle(self):
        random.shuffle(self.cards)

    def add_card(self, card):
        self.cards.append(card)

    def remove_card(self, card):
        self.cards.remove(card)

    def reveal_card(self, i=-1):
        return self.cards.pop(i)

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self, hand, num):
        for i in range(num):
            hand.add_card(self.reveal_card())


class Hand(Deck):

    def __init__(self):
        self.cards = []

    def remove(self):
        pass

    def __str__(self):
        res = []
        n=1
        for card in self.cards:
            res.append(str(n)+': '+str(card))
            n+=1
        return '\n'.join(res)

    def points_count(self):
        res = 0
        for card in self.cards:
            res+=card.points()
            print card.points()
        return res

if __name__ == "__main__":
    main()