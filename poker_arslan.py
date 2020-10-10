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
    hand= hand.replace('J','10')
    print(hand)

    p1=hand[:len(hand)//2]
    p2=hand[len(hand)//2:]
    print(p1)
    print(p2)
    p1_numbers=[]
    p1_suit=[]
    p2_numbers=[]
    p2_suit=[]

    for s in p1:
        
        if s.isdigit():
            p1_numbers.append(int(s))
        elif s=='J':
            p1_numbers.append(10)
        elif s=='Q':
            p1_numbers.append(11)
        elif s=='K':
            p1_numbers.append(12)
        elif s=='A':
            p1_numbers.append(13)
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
        

    
    return p1_numbers,p1_suit,p2_numbers,p2_suit

def find_winner(all_hands):

    for hand in all_hands:
        p1_numbers,p1_suit,p2_numbers,p2_suit=hand_format(hand)
        print(p1_numbers,p1_suit,p2_numbers,p2_suit)






find_winner(["9C 9D 8D 7C 3C 2S KD TH 9H 8H"])

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

