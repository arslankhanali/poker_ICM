#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 22:18:03 2020

@author: Arslan
"""
import sys
import timeit

def hand_format(hand):
    '''
    Converts a hand to a new format. 
            Parameters:
                    hands(list): e.g. [2H 9S 9C JD KH TD 4H JC 9H 8H] 
            Returns:
                    player1_numbers  -> [13, 11, 9, 9, 2]
                    player1_suit     -> ['C', 'D', 'H', 'H', 'S'] 
                    player2_numbers  -> [11, 10, 9, 8, 4] 
                    player2_suit     -> ['C', 'D', 'H', 'H', 'H']
                                                                 
            Assumptions:
                    T -> 10
                    J -> 11
                    Q -> 12
                    K -> 13
                    A -> 14
    '''
    #Remove any white spaces
    hand.strip()
    hand= hand.replace(' ','')

    #divide hands for player 1 and 2
    player1=hand[:len(hand)//2]
    player2=hand[len(hand)//2:]

    #initialize 
    player1_numbers=[]
    player1_suit=[]
    player2_numbers=[]
    player2_suit=[]

    #For player 1
    for s in player1:
        
        if s.isdigit():
            player1_numbers.append(int(s))
        elif s=='T':
            player1_numbers.append(10)
        elif s=='J':
            player1_numbers.append(11)
        elif s=='Q':
            player1_numbers.append(12)
        elif s=='K':
            player1_numbers.append(13)
        elif s=='A':
            player1_numbers.append(14)
        else:
            player1_suit.append(s)

    #For player 1
    for s in player2:
        if s.isdigit():
            player2_numbers.append(int(s))
        elif s=='T':
            player2_numbers.append(10)
        elif s=='J':
            player2_numbers.append(11)
        elif s=='Q':
            player2_numbers.append(12)
        elif s=='K':
            player2_numbers.append(13)
        elif s=='A':
            player2_numbers.append(14)
        else:
            player2_suit.append(s)
        
    # Sort in decenting order
    player1_numbers.sort(reverse=True)
    player2_numbers.sort(reverse=True)
    player1_suit.sort()
    player2_suit.sort()

    # Return
    return player1_numbers,player1_suit,player2_numbers,player2_suit

def royalflush(numbers,suit):
    '''
    Ten, Jack, Queen, King and Ace in the same suit
    '''
    #check if all cards have the same suit
    if suit.count('S')==5 or suit.count('D')==5 or suit.count('H')==5 or suit.count('C')==5:
        #check if we got 10,J,Q,K,A
        max_value=numbers[0]
        temp_list=list(range(max_value-4,max_value+1))
        temp_list.sort(reverse=True)
        if max_value==14 and numbers==temp_list:
            return True
    return False


def straightflush(numbers,suit):
    '''
    All five cards in consecutive value order, with the same suit
    '''
    if suit.count('S')==5 or suit.count('D')==5 or suit.count('H')==5 or suit.count('C')==5:
        max_value=numbers[0]
        temp_list=list(range(max_value-4,max_value+1))
        temp_list.sort(reverse=True)
        if numbers==temp_list:
            return numbers[0]
    return 0

def allpairs(numbers,suit):
    '''
    Finds all pairs in a hand.
        Parameter(list):
                [1, 1, J, J, 3]
        Returns(dict):
                {2:[11,1]}
    '''
    pairs={}
    for i in range(2,15):
        if numbers.count(i) > 0:
            if numbers.count(i) not in pairs.keys():
                pairs[numbers.count(i)]=i
            else:
                pairs[numbers.count(i)]=[pairs[numbers.count(i)],i]
    return pairs

def fourofakind(pairs):
    '''
    Four cards of the same value
    '''
    if 4 in pairs.keys():
        return pairs[4]
    return 0

def fullhouse(pairs):
    '''
    Three of a kind and a Pair
    '''
    if 3 in pairs.keys():
        if 2 in pairs.keys():
            ans=[pairs[3],pairs[2]]
            ans.sort(reverse=True)
            return ans
    return False


def flush(numbers,suit):
    '''
    All five cards having the same suit
    '''
    if suit.count('S')==5 or suit.count('D')==5 or suit.count('H')==5 or suit.count('C')==5:
        return True
    return False

def straight(numbers,suit):
    '''
    All five cards in consecutive value order
    '''
    i=numbers[0]
    l=list(range(i-4,i+1))
    l.sort(reverse=True)
    
    if numbers==l:
        return numbers[0]
    return 0


def threeofakind(pairs):
    '''
    Three cards of the same value
    '''
    if 3 in pairs.keys():
        return pairs[3]
    return 0


def twopair(pairs):
    '''
    Two different pairs
    '''
    if 2 in pairs.keys():
        if type(pairs[2]) == list:
            ans=pairs[2]
            ans.sort(reverse=True)
            return ans
    return False


def onepair(pairs):
    '''
    One pair
    '''
    if 2 in pairs.keys():
        if type(pairs[2]) != list:
            return pairs[2]
    return 0


def find_winner(all_hands):
    '''
    Finds how many hands each player won.

            Parameters:
                    all_hands(list): list of lists containing differents hands
            Returns:
                    [player1_wins,player2_wins]
            Assumption:
                    There is always one clear winner
                    A is only used as a high card
                    player1: represents player 1
                    player2: represents player 2
    '''
    player1_wins=0
    player2_wins=0

    for hand in all_hands:
        
        #Get hand in required format
        player1_numbers,player1_suit,player2_numbers,player2_suit=hand_format(hand)

        # print(player1_wins,player2_wins)
        # print(player1_numbers,player1_suit,player2_numbers,player2_suit)

        #Find all pairs in a dictionary format
        pairs=allpairs(player1_numbers,player1_suit)
        pairs2=allpairs(player2_numbers,player2_suit)

        #ROYAL FLUSH
        #---------------------------------
        royalflush_player1=royalflush(player1_numbers,player1_suit)
        royalflush_player2=royalflush(player2_numbers,player2_suit)
        # print('royal flush',royalflush_player1,royalflush_player2)
        if royalflush_player1 == royalflush_player2 == True:
            player1_wins+=1
            player2_wins+=1
        elif royalflush_player1>royalflush_player2:
            player1_wins+=1
        elif royalflush_player2>royalflush_player1:
            player2_wins+=1
        else:
            #STRAIGHT FLUSH
            #---------------------------------
            straightflush_player1=straightflush(player1_numbers,player1_suit)
            straightflush_player2=straightflush(player2_numbers,player2_suit)
            # print('straight flush',straightflush_player1,straightflush_player2)
            if straightflush_player1==straightflush_player2 and straightflush_player1 != 0:
                player1_wins+=1
                player2_wins+=1
            elif straightflush_player1>straightflush_player2:
                player1_wins+=1
            elif straightflush_player2>straightflush_player1:
                player2_wins+=1
            else:
                #FOUR OF A KIND
                #---------------------------------
                fourofakind_player1=fourofakind(pairs)
                fourofakind_player2=fourofakind(pairs2)
                # print('four of a kind',fourofakind_player1,fourofakind_player2)
                if fourofakind_player1==fourofakind_player2 and fourofakind_player1 != 0:
                    if player1_numbers>player2_numbers:
                        player1_wins+=1
                    else:
                        player2_wins+=1
                elif fourofakind_player1>fourofakind_player2:
                    player1_wins+=1
                elif fourofakind_player2>fourofakind_player1:
                    player2_wins+=1
                else:
                    #FULL HOUSE
                    #---------------------------------
                    fullhouse_player1=fullhouse(pairs)
                    fullhouse_player2=fullhouse(pairs2)
                    # print('fullhouse',fullhouse_player1,fullhouse_player2)
                    if fullhouse_player1==fullhouse_player2 and fullhouse_player1 != False:
                        if player1_numbers>player2_numbers:
                            player1_wins+=1
                        else:
                            player2_wins+=1
                    elif fullhouse_player2 == False and fullhouse_player1 != False:
                        player1_wins+=1
                    elif fullhouse_player1 == False and fullhouse_player2 != False:
                        player2_wins+=1
                    else:
                        #FLUSH
                        #---------------------------------
                        flush_player1=flush(player1_numbers,player1_suit)
                        flush_player2=flush(player2_numbers,player2_suit)
                        # print('flush',flush_player1,flush_player2)
                        if flush_player1==flush_player2 and flush_player1 != False:
                            player1_wins+=1
                            player2_wins+=1
                        elif flush_player1>flush_player2:
                            player1_wins+=1
                        elif flush_player2>flush_player1:
                            player2_wins+=1
                        else:
                            #STRAIGHT
                            #---------------------------------
                            straight_player1=straight(player1_numbers,player1_suit)
                            straight_player2=straight(player2_numbers,player2_suit)
                            # print('straight',sstraight_player1,straight_player2)
                            if straight_player1==straight_player2 and straight_player1!=0:
                                player1_wins+=1
                                player2_wins+=1
                            elif straight_player1>straight_player2:
                                player1_wins+=1
                            elif straight_player2>straight_player1:
                                player2_wins+=1
                            else:
                                #THREE OF A KIND
                                #---------------------------------
                                threeofakind_player1=threeofakind(pairs)
                                threeofakind_player2=threeofakind(pairs2)
                                # print('three of a kind',threeofakind_player1,threeofakind_player2)
                                if threeofakind_player1==threeofakind_player2 and threeofakind_player1 != 0:
                                    if player1_numbers>player2_numbers:
                                        player1_wins+=1
                                    else:
                                        player2_wins+=1
                                elif threeofakind_player1>threeofakind_player2:
                                    player1_wins+=1
                                elif threeofakind_player2>threeofakind_player1:
                                    player2_wins+=1
                                else:
                                    #TWO PAIR
                                    #---------------------------------
                                    twopairs_player1=twopair(pairs)
                                    twopairs_player2=twopair(pairs2)
                                    # print('two pairs',twopairs_player1,twopairs_player2)
                                    if twopairs_player1==twopairs_player2 and twopairs_player1 != False:
                                        if player1_numbers>player2_numbers:
                                            player1_wins+=1
                                        else:
                                            player2_wins+=1
                                    elif twopairs_player2==False and twopairs_player1 != False:
                                        player1_wins+=1
                                    elif twopairs_player1==False and twopairs_player2 != False:
                                        player2_wins+=1
                                    else:
                                        #ONE PAIR
                                        #---------------------------------
                                        onepair_player1=onepair(pairs)
                                        onepair_player2=onepair(pairs2)
                                        # print('one pair',onepair_player1,onepair_player2)
                                        if onepair_player1==onepair_player2 and onepair_player1 != 0:
                                            if player1_numbers>player2_numbers:
                                                player1_wins+=1
                                            else:
                                                player2_wins+=1
                                        elif onepair_player1>onepair_player2:
                                            player1_wins+=1
                                        elif onepair_player2>onepair_player1:
                                            player2_wins+=1
                                        else:
                                            #HIGHCARD
                                            #---------------------------------
                                            # print('highcard for player1 ',player1_numbers>player2_numbers)
                                            if player1_numbers>player2_numbers:
                                                player1_wins+=1
                                            elif player2_numbers>player1_numbers:
                                                player2_wins+=1
                                            

    print()
    print("        Player 1 : ",player1_wins,' hands')   
    print("        Player 2 : ",player2_wins,' hands')
    print("----------------------------------------")           
    return [player1_wins,player2_wins]


def testcases():
    '''
    Test cases for different scenerios 
    '''
    
    assert find_winner(["JC TC AC KC QC 2S KD TH 9H 8H"]) == [1,0], 'should be a royal flush'
    assert find_winner(["JC 2D 2C 2H 2S 2S KD TH 9H 8H"]) == [1,0], 'should be a 4 of a kind'
    assert find_winner(["JC JD 5C 5H 5S 2S KD TH 9H 8H"]) == [1,0], 'should be a fulhouse'
    assert find_winner(["6C 2C 2C 2C 2C 2S KD TH 9H 8H"]) == [1,0], 'should be a flush'
    assert find_winner(["7C 6D TC 9H 8S 2S KD TH 9H 8H"]) == [1,0], 'should be a straight'
    assert find_winner(["JC 2D 2C 9H 2S 2S KD TH 9H 8H"]) == [1,0], 'should be a 3 of a kind'
    assert find_winner(["AC 9D 9C 2H AS 2S KD TH 9H 8H"]) == [1,0], 'should be two pairs'
    assert find_winner(["JC 8D 8C AH 2S 2S KD TH 9H 8H"]) == [1,0], 'should be one pair'
    assert find_winner(["2C 3D 4C 4H 5S 2S KD TH 9H 8H"]) == [1,0], 'should be a highcard'

    print("All test cases passed!")

def validate_input(all_hands):
    '''
    Checks if the input is valid.
            Parameters:
                    all_hands(list): list of lists containing differents hands
            Returns:
                    Boolean: True if input is valid
    '''
    pass

if __name__ == "__main__":
    # testcases()

    print("----------------------------------------")
    print("    ICM coding submission by ARSLAN")
    print("Provide input and then hit enter twice: ")
    
    
    #Save input in a list all_hands
    all_hands=[]
    for line in iter(sys.stdin.readline, ''):
        if line=="\n":
            break
        all_hands.append(line.replace('\n',''))
    print("----------------------------------------")

    # validate_input(all_hands)

    #start time
    start = timeit.default_timer()

    #find winner between player 1 and 2
    try:
        find_winner(all_hands)
    except :
        print("  !Invalid input. Please cheack again!")
    
    #stop time
    stop = timeit.default_timer()

    #time taken. used to check efficiency
    print('Time Taken : ', stop - start,'sec')
    print("---------------ThankYou----------------") 