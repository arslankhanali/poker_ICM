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
            return numbers[-1]
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
        return pairs[3]
    return False


def twopair(pairs):
    if 2 in pairs.keys():
        if type(pairs[2]) == list:
            return pairs[2]
    return False


def onepair(pairs):
    if 2 in pairs.keys():
        if type(pairs[2]) != list:
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

        pairs=allpairs(p1_numbers,p1_suit)
        pairs2=allpairs(p2_numbers,p2_suit)

        #ROYAL FLUSH
        rf1=royalflush(p1_numbers,p1_suit)
        rf2=royalflush(p2_numbers,p2_suit)
        if rf1==rf2== True:
            p1_wins+=1
            p2_wins+=1
        elif rf1>rf2:
            p1_wins+=1
        elif rf2>rf1:
            p2_wins+=1
        else:
            #STRAIGHT FLUSH
            sf1=straightflush(p1_numbers,p1_suit)
            sf2=straightflush(p2_numbers,p2_suit)
            if sf1==sf2:
                p1_wins+=1
                p2_wins+=1
            elif sf1>sf2:
                p1_wins+=1
            elif sf2>sf1:
                p2_wins+=1
            else:
                #FOUR OF A KIND
                fok1=fourofakind(pairs)
                fok2=fourofakind(pairs2)
                if fok1==fok2:
                    p1_wins+=1
                    p2_wins+=1
                elif fok1>fok2:
                    p1_wins+=1
                elif fok2>fok1:
                    p2_wins+=1
                else:
                    #FULL HOUSE
                    fl1=fullhouse(p1_numbers,p1_suit)
                    fl2=fullhouse(p2_numbers,p2_suit)
                    if fl1==fl2:
                        p1_wins+=1
                        p2_wins+=1
                    elif fl1>fl2:
                        p1_wins+=1
                    elif fl2>fl1:
                        p2_wins+=1
                    else:
                        #FLUSH
                        f1=flush(p1_numbers,p1_suit)
                        f2=flush(p2_numbers,p2_suit)
                        if f1==f2:
                            p1_wins+=1
                            p2_wins+=1
                        elif f1>f2:
                            p1_wins+=1
                        elif f2>f1:
                            p2_wins+=1
                        else:
                            #STRAIGHT
                            s1=straight(p1_numbers,p1_suit)
                            s2=straight(p2_numbers,p2_suit)
                            if s1==s2:
                                p1_wins+=1
                                p2_wins+=1
                            elif s1>s2:
                                p1_wins+=1
                            elif s2>s1:
                                p2_wins+=1
                            else:
                                #THREE OF A KIND
                                tok1=threeofakind(pairs)
                                tok2=threeofakind(pairs2)
                                if tok1==tok2:
                                    p1_wins+=1
                                    p2_wins+=1
                                elif tok1>tok2:
                                    p1_wins+=1
                                elif tok2>tok1:
                                    p2_wins+=1
                                else:
                                    #TWO PAIR
                                    tp1=twopair(pairs)
                                    tp2=twopair(pairs2)
                                    if tp1==tp2:
                                        p1_wins+=1
                                        p2_wins+=1
                                    elif tp1>tp2:
                                        p1_wins+=1
                                    elif tp2>tp1:
                                        p2_wins+=1
                                    else:
                                        #ONE PAIR
                                        op1=onepair(pairs)
                                        op2=
                                        if op1==op2:
                                            p1_wins+=1
                                            p2_wins+=1
                                        elif op1>op2
                                            p1_wins+=1
                                        elif op2>op1:
                                            p2_wins+=1
                                        else:
                                            #HIGHCARD
                                            hc1=highcard(p1_numbers,p1_suit)
                                            hc2=highcard(p2_numbers,p2_suit)
                                            if hc1==hc2:
                                                p1_wins+=1
                                                p2_wins+=1
                                            elif hc1>hc2:
                                                p1_wins+=1
                                            elif hc2>hc1:
                                                p2_wins+=1
                                            else:
                                                continue



            



        # print(royalflush(p1_numbers,p1_suit))
        # print(straightflush(p1_numbers,p1_suit))
        pairs=allpairs(p1_numbers,p1_suit)
        print(pairs)

        print(fourofakind(pairs))
        print(fullhouse(pairs))
        # return fullhouse(pairs)
        print(flush(p1_numbers,p1_suit))
        print(straigh(p1_numbers,p1_suit))
        print(threeofakind(pairs))
        print(twopair(pairs))
        print(onepair(pairs))
        print(highcard(p1_numbers,p1_suit))
        






# find_winner(["9C 9D 8D 7C 3C 2S KD TH 9H 8H"]) 
# assert find_winner(["JC TC AC KC QC 2S KD TH 9H 8H"])==True, 'not a royal flush'

# assert find_winner(["JC 2D 2C 2H 2S 2S KD TH 9H 8H"])== 2, 'not a 4ofakind
# assert (find_winner(["JC JD 5C 5H 5S 2S KD TH 9H 8H"])) == [5,11], 'not a fulhouse'
# assert find_winner(["6C 2C 2C 2C 2C 2S KD TH 9H 8H"]) == True, 'not a flush'
# assert find_winner(["7C 6D TC 9H 8S 2S KD TH 9H 8H"]) == True, 'not straight'
# assert find_winner(["JC 2D 2C 9H 2S 2S KD TH 9H 8H"]) == 8, 'not 3kind'
# assert find_winner(["AC 9D 9C 2H AS 2S KD TH 9H 8H"]) ==[9,14], 'not 2,2'
# assert find_winner(["JC 8D 8C AH 2S 2S KD TH 9H 8H"]) == 8 , 'not 2'
# assert find_winner(["2C 3D 4C 4H 5S 2S KD TH 9H 8H"]) == 5, '5 not highcard'

#if __name__ == "__main__":
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

