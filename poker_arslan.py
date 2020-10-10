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
        

    p1_numbers.sort(reverse=True)
    p2_numbers.sort(reverse=True)
    p1_suit.sort()
    p2_suit.sort()
    return p1_numbers,p1_suit,p2_numbers,p2_suit

def royalflush(numbers,suit):
    if suit.count('S')==5 or suit.count('D')==5 or suit.count('H')==5 or suit.count('C')==5:
        i=numbers[0]
        l=list(range(i-4,i+1))
        l.sort(reverse=True)
        if i==14 and numbers==l:
            return True
    return False


def straightflush(numbers,suit):
    if suit.count('S')==5 or suit.count('D')==5 or suit.count('H')==5 or suit.count('C')==5:
        i=numbers[0]
        l=list(range(i-4,i+1))
        l.sort(reverse=True)
        if numbers==l:
            return numbers[0]
    return 0

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
    return 0

def fullhouse(pairs):
    if 3 in pairs.keys():
        if 2 in pairs.keys():
            ans=[pairs[3],pairs[2]]
            ans.sort(reverse=True)
            return ans
    return False


def flush(numbers,suit):
    if suit.count('S')==5 or suit.count('D')==5 or suit.count('H')==5 or suit.count('C')==5:
        return True
    return False

def straight(numbers,suit):
    i=numbers[0]
    l=list(range(i-4,i+1))
    l.sort(reverse=True)
    
    if numbers==l:
        return numbers[0]
    return 0


def threeofakind(pairs):
    if 3 in pairs.keys():
        return pairs[3]
    return 0


def twopair(pairs):
    if 2 in pairs.keys():
        if type(pairs[2]) == list:
            ans=pairs[2]
            ans.sort(reverse=True)
            return ans
    return False


def onepair(pairs):
    if 2 in pairs.keys():
        if type(pairs[2]) != list:
            return pairs[2]
    return 0




def find_winner(all_hands):
    p1_wins=0
    p2_wins=0

    for hand in all_hands:

        p1_numbers,p1_suit,p2_numbers,p2_suit=hand_format(hand)
        print(p1_wins,p2_wins)
        print(p1_numbers,p1_suit,p2_numbers,p2_suit)

        pairs=allpairs(p1_numbers,p1_suit)
        pairs2=allpairs(p2_numbers,p2_suit)

        #ROYAL FLUSH
        rf1=royalflush(p1_numbers,p1_suit)
        rf2=royalflush(p2_numbers,p2_suit)
        # print('royal flush',rf1,rf2)
        if rf1 == rf2 == True:
            p1_wins+=1
            p2_wins+=1
        elif rf1>rf2:
            p1_wins+=1
            print("p1 rf")
        elif rf2>rf1:
            p2_wins+=1
        else:
            #STRAIGHT FLUSH
            sf1=straightflush(p1_numbers,p1_suit)
            sf2=straightflush(p2_numbers,p2_suit)
            # print('straight flush',sf1,sf2)
            if sf1==sf2 and sf1 != 0:
                p1_wins+=1
                p2_wins+=1
            elif sf1>sf2:
                p1_wins+=1
                print("p1 sf")
            elif sf2>sf1:
                p2_wins+=1
            else:
                #FOUR OF A KIND
                fok1=fourofakind(pairs)
                fok2=fourofakind(pairs2)
                # print('four of a kind',fok1,fok2)
                if fok1==fok2 and fok1 != 0:
                    if p1_numbers>p2_numbers:
                        p1_wins+=1
                    else:
                        p2_wins+=1
                elif fok1>fok2:
                    p1_wins+=1
                    print("p1 fok")
                elif fok2>fok1:
                    p2_wins+=1
                else:
                    #FULL HOUSE
                    fl1=fullhouse(pairs)
                    fl2=fullhouse(pairs2)
                    # print('fullhouse',fl1,fl2)
                    if fl1==fl2 and fl1 != False:
                        if p1_numbers>p2_numbers:
                            p1_wins+=1
                        else:
                            p2_wins+=1
                    elif fl2 == False and fl1 != False:
                        p1_wins+=1
                        print("p1 fl")
                    elif fl1 == False and fl2 != False:
                        p2_wins+=1
                    else:
                        #FLUSH
                        f1=flush(p1_numbers,p1_suit)
                        f2=flush(p2_numbers,p2_suit)
                        # print('flush',f1,f2)
                        if f1==f2 and f1 != False:
                            p1_wins+=1
                            p2_wins+=1
                        elif f1>f2:
                            p1_wins+=1
                            print("p1 f")
                        elif f2>f1:
                            p2_wins+=1
                        else:
                            #STRAIGHT
                            s1=straight(p1_numbers,p1_suit)
                            s2=straight(p2_numbers,p2_suit)
                            print('straight',s1,s2)
                            if s1==s2 and s1!=0:
                                p1_wins+=1
                                p2_wins+=1
                            elif s1>s2:
                                print("p1 s")
                                p1_wins+=1
                            elif s2>s1:
                                p2_wins+=1
                                
                            else:
                                #THREE OF A KIND
                                tok1=threeofakind(pairs)
                                tok2=threeofakind(pairs2)
                                # print('three of a kind',tok1,tok2)
                                if tok1==tok2 and tok1 != 0:
                                    if p1_numbers>p2_numbers:
                                        p1_wins+=1
                                    else:
                                        p2_wins+=1
                                elif tok1>tok2:
                                    p1_wins+=1
                                    print("p1 tok")
                                elif tok2>tok1:
                                    p2_wins+=1
                                else:
                                    #TWO PAIR
                                    tp1=twopair(pairs)
                                    tp2=twopair(pairs2)
                                    # print('two pairs',tp1,tp2)
                                    if tp1==tp2 and tp1 != False:
                                        if p1_numbers>p2_numbers:
                                            p1_wins+=1
                                        else:
                                            p2_wins+=1
                                    elif tp2==False and tp1 != False:
                                        p1_wins+=1
                                        print("p1 tp")
                                    elif tp1==False and tp2 != False:
                                        p2_wins+=1
                                    else:
                                        #ONE PAIR
                                        op1=onepair(pairs)
                                        op2=onepair(pairs2)
                                        # print('one pair',op1,op2)
                                        if op1==op2 and op1 != 0:
                                            if p1_numbers>p2_numbers:
                                                p1_wins+=1
                                            else:
                                                p2_wins+=1
                                        elif op1>op2:
                                            p1_wins+=1
                                        elif op2>op1:
                                            p2_wins+=1
                                        else:
                                            #HIGHCARD
                                            # print('highcard for p1 ',p1_numbers>p2_numbers)
                                            if p1_numbers>p2_numbers:
                                                p1_wins+=1
                                            elif p2_numbers>p1_numbers:
                                                p2_wins+=1
                                            


    print("Player 1 : ",p1_wins)   
    print("Player 2 : ",p2_wins)           
    return [p1_wins,p2_wins]


def testcases():
    
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
    pass

if __name__ == "__main__":
    testcases()
    print("ICM coding submission by Arslan")
    print("Provide input and then hit enter twice: ")
    
    all_hands=[]
    for line in iter(sys.stdin.readline, ''):
        if line=="\n":
            break
        all_hands.append(line.replace('\n',''))

    # validate_input(all_hands)
    find_winner(all_hands)

