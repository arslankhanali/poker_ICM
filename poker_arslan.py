#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 22:18:03 2020

@author: Arslan
"""
import sys

def hand_format(hand):
    hand.strip()
    hand= hand.replace(' ','')

    p1=hand[:len(hand)//2]
    p2=hand[len(hand)//2:]

    p1_numbers=[]
    p1_suit=[]
    p2_numbers=[]
    p2_suit=[]

    for s in p1:
        
        if s.isdigit():
            p1_numbers.append(int(s))
        elif s=='T':
            p1_numbers.append(10)
        elif s=='J':
            p1_numbers.append(11)
        elif s=='Q':
            p1_numbers.append(12)
        elif s=='K':
            p1_numbers.append(13)
        elif s=='A':
            p1_numbers.append(14)
        else:
            p1_suit.append(s)

    for s in p2:
        if s.isdigit():
            p2_numbers.append(int(s))
        elif s=='T':
            p2_numbers.append(10)
        elif s=='J':
            p2_numbers.append(11)
        elif s=='Q':
            p2_numbers.append(12)
        elif s=='K':
            p2_numbers.append(13)
        elif s=='A':
            p2_numbers.append(14)
        else:
            p2_suit.append(s)
        

    p1_numbers.sort()
    p2_numbers.sort()
    p1_suit.sort()
    p2_suit.sort()
    return p1_numbers,p1_suit,p2_numbers,p2_suit

def royalflush(numbers,suit):
    if suit.count('S')==5 or suit.count('D')==5 or suit.count('H')==5 or suit.count('C')==5:
        if numbers[0]==10 and numbers[-1]==14:
            return True
    return False


def straightflush(numbers,suit):
    if suit.count('S')==5 or suit.count('D')==5 or suit.count('H')==5 or suit.count('C')==5:
        if numbers[-1]-numbers[0] == 4:
            return True
    return False

def allpairs(numbers,suit):
    pairs={}
    for i in range(2,15):
        if numbers.count(i) > 0:
            if numbers.count(i) not in pairs.keys():
                pairs[numbers.count(i)]=i
            else:
                pairs[numbers.count(i)]=[pairs[numbers.count(i)],i]
    return pairs

def fourofakind(pairs):
    if 4 in pairs.keys():
        return pairs[4]
    return False

def fullhouse(pairs):
    if 3 in pairs.keys():
        if 2 in pairs.keys():
            return [pairs[3],pairs[2]]
    return False


def flush(numbers,suit):
    if suit.count('S')==5 or suit.count('D')==5 or suit.count('H')==5 or suit.count('C')==5:
        return True
    return False

def striagh(numbers,suit):
    if numbers[-1]-numbers[0] == 4:
            return True
    return False

def threeofakind(pairs):
    if 3 in pairs.keys():
        return pairs[4]
    return False


def twopair(pairs):
    if 2 in pairs.keys():
        if type(pairs[2]) == list
        return pairs[2].sort()
    return False


def onepair(pairs):
    if 2 in pairs.keys():
        if type(pairs[2]) != list
        return pairs[2]
    return False

def highcard(numbers,suit):
    return max(numbers)



def find_winner(all_hands):

    for hand in all_hands:

        p1_wins=0
        p2_wins=0

        p1_numbers,p1_suit,p2_numbers,p2_suit=hand_format(hand)
        print(p1_numbers,p1_suit,p2_numbers,p2_suit)

        # print(royalflush(p1_numbers,p1_suit))
        # print(straightflush(p1_numbers,p1_suit))
        pairs=allpairs(p1_numbers,p1_suit)
        print(pairs)
        print(fourofakind(pairs))
        print(fullhouse(pairs))
        print(flush(pairs))
        print(striagh(pairs))
        print(threeofakind(pairs))
        print(twopair(pairs))
        print(onepair(pairs))
        print(highcard(pairs))
        






# find_winner(["9C 9D 8D 7C 3C 2S KD TH 9H 8H"]) 
# find_winner(["JC TC AC KC QC 2S KD TH 9H 8H"]) #royal flush

find_winner(["JC 2D 2C 2H 2S 2S KD TH 9H 8H"]) #4ofakind

# if __name__ == "__main__":
#     print("Welcome to Poker hand sorter by ARSLAN!!!")
#     print("Provide hands for each player in the format \
# 'AH 9S 4D TD 8S 4H JS 3C TC 8D', where the first 5 \
# cards in the line have been dealt to Player 1 and last 5 to player 2")
#     print("Hit enter twice when you have added all hands")
#     all_hands=[]
#     for line in iter(sys.stdin.readline, ''):
#         if line=="\n":
#             break
        
#         all_hands.append(line.replace('\n',''))

    # print("Following hands added")
    # for hand in all_hands:
    #     print(hand)

