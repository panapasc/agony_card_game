import random


# agony card game


# --------------------Deck of cards class--------------------
class Deck():
    # card deck list.
    # 2D list
    #           s: spades, c: clubs, d: diamonds, h: heart
    cards = ('As', 'Ac', 'Ad', 'Ah',
             '2s', '2c', '2d', '2h',
             '3s', '3c', '3d', '3h',
             '4s', '4c', '4d', '4h',
             '5s', '5c', '5d', '5h',
             '6s', '6c', '6d', '6h',
             '7s', '7c', '7d', '7h',
             '8s', '8c', '8d', '8h',
             '9s', '9c', '9d', '9h',
             '10s', '10c', '10d', '10h',
             'Js', 'Jc', 'Jd', 'Jh',
             'Qs', 'Qc', 'Qd', 'Qh',
             'Ks', 'Kc', 'Kd', 'Kh'
             )
    deck_of_cards = list(cards)

    def shuffle_deck(self):
        random.shuffle(self.deck_of_cards)

    def deal_to_player(self, player_object):  # deal hand to the player object
        hand = []
        for i in range(0, 7, 1):
            hand.append(self.deck_of_cards.pop(-1))  # pop last deck_of_cards element and put it in hand list
        player_object.get_hand(hand)
        # print('hand is: ',hand) #DEBUGGING

    def give_card_from_deck(self):
        return self.deck_of_cards.pop(-1)


# unicode card shapes
spades_unicode = "\u2663"  # spades
clubs_unicode = "\u2660"  # clubs
diamonds_unicode = "\u2666"  # diamonds
hearts_unicode = "\u2665"  # hearts


# ---------------------Player class---------------------
class Player():
    hand = []

    def __init__(self, x, y):  # get players name and id on initialization
        self.name = x
        self.id = y

    def get_hand(self, a):
        self.hand = a

    def print_cards(self):  # prints cards held b player
        for i in self.hand[:]:
            if i[-1] == 's':
                print(i[:-1] + spades_unicode, end="  ")  # end=="" prints next time in the same line
            elif i[-1] == 'c':
                print(i[:-1] + clubs_unicode, end="  ")
            elif i[-1] == 'd':
                print(i[:-1] + diamonds_unicode, end="  ")
            elif i[-1] == 'h':
                print(i[:-1] + hearts_unicode, end="  ")
        print('\n')

    def my_choice(self):
        self.print_cards()
        print('1.Play card     2.Draw from deck')
        while True:
            try:
                print(self.name,end=' ')
                choice = int(input('Enter choice:'))
            except ValueError:
                print('Not valid input. Input must be an integer')
            else:
                if choice == 1 or choice == 2:
                    return choice
                else:
                    print('Input not valid. Try again')

    def play_card(self):  # card 'a' is picked by player
        while True:
            card = str(input("Enter the card you want to play "+str(self.name)))
            if card in self.hand:
                break
            else:
                print('Your input was invalid or you do not have that card. 10 diamond example: 10d ')
        for i in range(len(self.hand)):
            if card == self.hand[i]:
                x = i
                break
        self.hand.pop(x)
        return card


# -----------------Game class-----------------
class Game():
    # Game class variables
    table_card_stack = []
    game_id = 0  # game number in case of consecutive matches
    players = []  # list of player objects
    wins = []  # a list with the wins for each player object
    dealer_index = None  # player that is the dealer. This variable is the index from the players list
    number_of_players = 0
    player_index = 0  # index for who is playing now
    seven_counter = 0
    top_card_kind = '0'
    rounds_played = 0

    # Game class functions
    def __init__(self):
        self.game_id = 1
        self.deck_object = Deck()

    # this function selects the number of players which must be 2 or 4
    def select_players(self, y=None):
        if y==None:
            x = 0
            while True:
                try:
                    x = int(input('Please input 2 or 4 as number of players'))
                except ValueError:
                    pass
                if x == 2 or x == 4:
                    break
                else:
                    print('Invalid entry')
            self.number_of_players = x
        else:
            self.number_of_players = y

    def assign_human_players(self):
            for i in range(0, self.number_of_players, 1):
                j = str(input('Please input name of #' + str(i + 1) + ' player'))
                self.players.append(Player(j, i + 1))   # create player objects
                self.wins = [0]*self.number_of_players  # initialises the wins list with zeros
            del self.number_of_players  # free memory by deleting number of players. len(players) now holds that information

    # sets the dealer. For the first game he is picked randomly but for the next ones
    #  its the next player from the players list
    def set_dealer(self):
        if self.game_id == 1 and self.dealer_index is None:
            self.dealer_index = random.randrange(0, len(self.players))
            print('The dealer is: '+str(self.players[self.dealer_index].name))
        else:
            self.index_plus_one('dealer')

    def deal(self):  # deal to every player and first time to table too
        self.deck_object.shuffle_deck()
        self.table_card_stack.append(
            self.deck_object.deck_of_cards.pop(-1))  # leaves one card on table for the first round
        self.set_dealer()  # sets the dealer
        # print('dealer is: '+str(self.dealer_index)) #DEBUGGING
        x = self.dealer_index + 1  # index for dealing to start from the person next to the dealer
        for i in range(0, len(self.players)):
            if x >= len(self.players):
                x = 0  # overflow protection
            self.deck_object.deal_to_player(self.players[x])  # this line deals the hands to every player by
            # print('players index:'+str(x))  #DEBUGGING
            self.players[x].print_cards()
            # calling deal_to_player function with deck_object
            x += 1
        self.top_card_kind = self.table_card_stack[-1][-1]

    def play_by_turn(self):
        self.set_dealer()
        self.deal()
        self.rounds_played+=1
        #DEBUGGING_ON
        (gob.players[0]).hand.pop(-1)
        (gob.players[0]).hand.pop(-1)
        (gob.players[0]).hand.pop(-1)
        (gob.players[0]).hand.pop(-1)
        (gob.players[0]).hand.pop(-1)
        (gob.players[0]).hand.pop(-1)

        (gob.players[1]).hand.pop(-1)
        (gob.players[1]).hand.pop(-1)
        (gob.players[1]).hand.pop(-1)
        (gob.players[1]).hand.pop(-1)
        (gob.players[1]).hand.pop(-1)
        (gob.players[1]).hand.pop(-1)
        # DEBUGGING_OFF
        while True:
            if self.check_if_win() is True:
                while True:
                    x = int(input('Press 1 for new game or 2 to quit'))
                    if x == 1:
                        self.star_new_game()
                        break
                    elif x == 2:
                        exit(0)
                    else:
                        print('Invalid input. Try again')
                break
            else:
                self.player_play(self.players[self.player_index])


    def player_play(self, player_object):  # when this is called the player must play
        top_card = self.table_card_stack[-1]
        # if card on table is 7 call the get cards penalty function. If a 7 is dealt the player will not take the penalty
        if top_card[:-1] == '7' and self.rounds_played>1:
            self.get_cards_penalty(player_object)
        print('top card: ' + str(self.table_card_stack[-1]))
        print('top kind: ' + self.top_card_kind)
        choice = player_object.my_choice()  # 1.Play card     2.Draw from deck
        if choice == 2:
            self.draw_card_from_deck(player_object)
            player_object.print_cards()
            while True:
                choice2 = int(input('press 1 to play or 2 to fold'))
                if choice2 == 1:    # play a card
                    choice = 1
                    break
                elif choice2 == 2:  # end players turn
                    self.end_turn('0')
                    break
                else:
                    print('Invalid input. Try again...')
        if choice == 1:
            while True:
                card = player_object.play_card()  # calls play func from Players class for every player object
                leg = self.check_if_card_is_legal(card)
                if leg is True:
                    if card[:-1] == 'A':
                        while True:
                            x = str(input('Choose what kind you want this to be\ns for spades, c for clubs, d for diamonds and h for hearts'))
                            if x == 's' or x == 'c' or x == 'd' or x == 'h':
                                self.top_card_kind = x[0]
                                break
                            else:
                                print('invalid input. Please try again')
                    self.table_card_stack.append(card)
                    self.end_turn(card)
                    break

    # checks if a player won the game. returns true if someone won and false otherwise
    def check_if_win(self):
        for index, i in enumerate(self.players):
            if len(i.hand) <= 0:
                self.wins[index] += 1
                #print(str(i.name) + ' won this game!')             #DEBUGGING_ONLY
                return True
        return False

    # pointer-like variable player or dealer index increase.
    # If it reaches the end of the list starts from 0 again
    def index_plus_one(self,a):
        if a == 'player':
            x = self.player_index
            x += 1
            if x >= len(self.players):
                x = 0
            self.player_index = x
        elif a == 'dealer':
            x = self.dealer_index
            x += 1
            if x >= len(self.players):
                x = 0
            self.dealer_index = x

    # either gets the cards from  a 7 played by a previous player
    # or plays 7 to pass the penalty to next player
    def get_cards_penalty(self, player_object):
        # DEBUGGING
        print('\nThere was a 7 on the table, so player: '+str(player_object.name)+' has to take some cards')
        while True:
            x = int(input('press 1 to take ' + str(2*self.seven_counter) + ' cards or 2 if you have a 7 to play'))
            if x == 2:
                if ('7s' not in player_object.hand) and ('7c' not in player_object.hand) and ('7d' not in player_object.hand) and ('7h' not in player_object.hand):
                    print('you don\'t have a 7 to play')
                    x = 1
                else:
                    y =player_object.play_card()
                    while y[:-1]!='7':
                        print('Illegal move. Please choose a 7')
                        self.give_card_to_player(player_object,y)
                        y = player_object.play_card()
                    self.table_card_stack.append(y)
                    self.top_card_kind = y[-1]
                    self.seven_counter += 1
                    break
            if x == 1:
                for i in range(2*self.seven_counter):
                    self.draw_card_from_deck(player_object)
                print('Player ' + str(player_object.name) + 'has taken ' + str(2 * self.seven_counter) + ' cards')
                self.seven_counter = 0
                break
            else:
                print('Your input is invalid. Please try again')

    def end_turn(self, last_card_played):
        if last_card_played[0]!='A':
            self.top_card_kind = self.table_card_stack[-1][-1]
        if self.check_if_win() is False :
            if last_card_played[:-1]=='8':      # same player must play again
                pass
            elif last_card_played[:-1]=='9':      # next player losses turn
                self.index_plus_one('player')
                self.index_plus_one('player')
            elif last_card_played[:-1]=='7':
                self.seven_counter+=1
                self.index_plus_one('player')
            else:
                self.index_plus_one('player')




    def draw_card_from_deck(self, player_object):
        self.full_deck_if_empty()
        player_object.hand.append(self.deck_object.deck_of_cards.pop(-1))

    # checks if deck is empty. If so, takes table card stack (leaving the last element(top card)),
    #  shuffles it and gives it to deck of cards
    def full_deck_if_empty(self):
        if len(self.deck_object.deck_of_cards) <= 0:
            for i in self.table_card_stack[:-1]:
                self.deck_object.deck_of_cards.append(i)
                self.table_card_stack.pop(0)
        self.deck_object.shuffle_deck()

    def star_new_game(self):
        self.game_id += 1
        for i in self.players:
            i.hand.clear()      # clears players hand
        self.rounds_played = 0
        self.play_by_turn()

    def check_if_card_is_legal(self, card):
        top_card = self.table_card_stack[-1]
        if card[:-1]=='A' and top_card[:-1]!='A':
            return True
        # you must play  the same number or the same kin or ace.You cant play ace on ace
        if (card[-1] != self.top_card_kind and card[:-1] != top_card[:-1]) or (top_card[0] == 'A' and card[0] == 'A'):
            print('You can\'t play that card')
            self.give_card_to_player(self.players[self.player_index],card)
            print('Card '+str(card)+' is illegal')
            return False
        else:
            return True

    # Gives players card back in case of an illegal move
    def give_card_to_player(self, player_object, card):
        player_object.hand.append(card)


# -----------------main program-----------------

gob = Game()
gob.select_players(2)
gob.assign_human_players()


#gob.deal()
gob.play_by_turn()



