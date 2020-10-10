#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 22:18:03 2020

@author: Arslan
"""
import sys

def 


if __name__ == "__main__":
    print("Welcome to Poker hand sorter by ARSLAN!!!")
    print("Provide hands for each player in the format \
'AH 9S 4D TD 8S 4H JS 3C TC 8D', where the first 5 \
cards in the line have been dealt to Player 1 and last 5 to player 2")
    print("Hit enter twice when you have added all hands")
    all_hands=[]
    for line in iter(sys.stdin.readline, ''):
        if line=="\n":
            break
        
        all_hands.append(line.replace('\n',''))

    print("Following hands added")
    for hand in all_hands:
        print(hand)

