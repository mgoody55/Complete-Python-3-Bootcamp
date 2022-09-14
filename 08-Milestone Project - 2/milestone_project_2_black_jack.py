import random

'''
In this milestone project you will be creating a Complete BlackJack Card Game in Python.

Here are the requirements:

- You need to create a simple text-based BlackJack game
- The game needs to have one player versus an automated dealer.
- The player can stand or hit.
- The player must be able to pick their betting amount.
- You need to keep track of the player's total money.
- You need to alert the player of wins, losses, or busts, etc...

And most importantly:
    You must use OOP and classes in some portion of your game. 
    You can not just use functions in your game. Use classes to help you 
    define the Deck and the Player's hand. There are many right ways to do this, 
    so explore it well!
'''

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:
    def __init__(self):
        self.all_cards = [] 
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit,rank))
                
    def shuffle(self):
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        return self.all_cards.pop()

    def cut(self):
        cut_pos = int(input('Input cut position: '))
        cut_deck = self.all_cards[cut_pos:]
        cut_deck.extend(self.all_cards[:cut_pos]) 
        self.all_cards = cut_deck


class Player:
    balance = 100

    def __init__(self,name):
        self.name = name
        self.all_cards = []
        
    def remove_one(self):
        return self.all_cards.pop(0)
    
    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
#Broken        
    def print_cards(self):
        print(f'{self.name} has the:')
        for i, card in enumerate(self.all_cards):
            print(card)

        value_sum = 0
        for i, card in enumerate(self.all_cards):
            value_sum += self.all_cards[i]
        print(value_sum)
        

    def bet(self):
        ammount = int(input('Please enter your bet: '))
        self.balance -= ammount
        return ammount

    def won(self, ammount):
        self.balance += ammount

    def stand(self):
        pass

    def hit(self):
        pass

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'

#Game Setup
player_one = Player(input('Input Player Name: '))
dealer = Player('Dealer')

game_deck = Deck()
game_deck.shuffle()
game_deck.cut()

game_on = True

while game_on:
    #Bets
    p1_bet = player_one.bet()

    #Deal Hand
    for i in range(2):
        player_one.add_cards(game_deck.deal_one())
        dealer.add_cards(game_deck.deal_one())

    player_one.print_cards()


    #Check for Naturals


    #Splitting Pairs/Doubling Down - TBD


    #Player Stand or Hit - Check for bust after each play


    #Dealers Play


    #Resuffle Deck
    break