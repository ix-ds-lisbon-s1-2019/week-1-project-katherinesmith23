# -*- coding: utf-8 -*-
"""
Spyder Editor

@author Katherine Smith
"""
import random 
import copy

class PokerGame:
    
    #initialize the game
    def __init__(self):
        try:
            self.number_of_players = int(input("Number of Players? "))
        except ValueError: # We will catch ValueErrors but not other kinds of errors
            print("Error: This is not a valid number of players")
        
        
    #create a list of all the players in the game
    def names(self):
        self.players_list = []
        for i in range(self.number_of_players):
            name = input(f"Player {i+1}: ")
            self.players_list.append(name)
    
    
    #deal out cards to each player in the game
    def deal_cards(self):
        #accounts for all 52 possible cards, these are split up equally into
        #the four different suits
        #replaced the face cards with number values to simplify the comparison
        self.all_cards = [2,3,4,5,6,7,8,9,10,11,12,13,14, \
                          2,3,4,5,6,7,8,9,10,11,12,13,14, \
                          2,3,4,5,6,7,8,9,10,11,12,13,14, \
                          2,3,4,5,6,7,8,9,10,11,12,13,14]
        
        #creates a dictionary with the players as the keys and sorted lists of 
        #their cards as the values
        self.player_hands = {}
        for i in self.players_list:
            card_list = []
            for j in range(5):
                card = random.choice(self.all_cards)
                index = self.all_cards.index(card)
                self.all_cards.pop(index)
                card_list.append(card)
            card_list.sort(reverse = True)
            self.player_hands[i] = card_list
        
        #creates a dictionary that will print out the players' hands 
        #replaces the number values with the actual face cards
        self.print_version_hand = copy.deepcopy(self.player_hands)
        for i in self.players_list:
            if 14 in self.print_version_hand[i]:
                indices = [i for i, x in enumerate(self.print_version_hand[i])\
                           if x == 14]
                indices.sort(reverse=True)
                for j in indices:
                    self.print_version_hand[i].pop(j)
                    self.print_version_hand[i].append('A')
            if 13 in self.print_version_hand[i]:
                indices = [i for i, x in enumerate(self.print_version_hand[i])\
                           if x == 13]
                indices.sort(reverse=True)
                for j in indices:
                    self.print_version_hand[i].pop(j)
                    self.print_version_hand[i].append('K')
            if 12 in self.print_version_hand[i]:
                indices = [i for i, x in enumerate(self.print_version_hand[i])\
                           if x == 12]
                indices.sort(reverse=True)
                for j in indices:
                    self.print_version_hand[i].pop(j)
                    self.print_version_hand[i].append('Q')
            if 11 in self.print_version_hand[i]:
                indices = [i for i, x in enumerate(self.print_version_hand[i])\
                           if x == 11]
                indices.sort(reverse=True)
                for j in indices:
                    self.print_version_hand[i].pop(j)
                    self.print_version_hand[i].append('J')
            
        print(self.print_version_hand)


    #compares the hands of all the players and finds the winner
    def compare_cards(self):
        z = 0
        self.winners = self.players_list.copy()
        
        #goes through each player's hand and checks to see if their highest
        #number is larger than the max. if it is larger, they become the new
        #winner. if it is the same, they are added to the winners list, 
        #illustrating a tie. this loops through all 5 of the players cards, 
        #stopping when there is only one winner or when all of the cards
        #have been compared.
        while (z < 5) and (len(self.winners) > 1):
            max = 1
            for i in self.winners:
                if self.player_hands[i][z] > max:
                    self.winners = [i]
                    max = self.player_hands[i][z]
                if self.player_hands[i][z] == max:
                    if i not in self.winners:
                        self.winners.append(i)
            z += 1
            
        print("The winner is: " + self.winners[0])


def main(game):
    game.names()
    game.deal_cards()
    game.compare_cards()


if __name__ == "__main__":
    game1 = PokerGame()
    main(game1)
