# Poker Hand Sorter
Build a command line program that takes, via STDIN, a "stream" of hands for a two-player poker game. At the completion of the stream, your program should print to STDOUT the number of hands won by Player 1, and the number of hands won by Player 2.

## Requirments 
Python 3.7.6     
Test file "poker-hands.txt" in the same folder.

## How to Run
Open terminal and type
```python
$ cat poker-hands.txt | ./poker_arslan.py
```
or    
```python
$ cat poker-hands.txt | python3 poker_arslan.py
```

Expected output 
```python
        Player 1 :  263  hands    
        Player 2 :  237  hands
```
## Features 

* Passed the provided test file and took just 0.01sec
* README.md file for GitHub.
* Efficient solution. Provides the execution time as well.
* Presentable interface. Easy to use.
* Doc-strings for each function.
* Detailed comments.
* Meaningful variable names.
* Code is written to ease future development.
* Provides test cases.
* ToDO list if someone wants to make it into a full program.


## Assumptions
There is always a clear winner.    
'T' represents 10    
'A' is used only as a high card.    

## Input
Each line read via STDIN will be a set of 10 cards. Each card is represented by 2 characters - the value and the suit. The first 5 cards in the line have been dealt to Player 1, the last 5 cards in the line belong to Player 2.
##### For example
AH 9S 4D TD 8S 4H JS 3C TC 8D

## Output
At the completion of the stream into STDIN (EOF), the output of your file (in STDOUT) must clearly state how many hands Player 1 won, and how many hands Player 2 won.
##### For example
Player 1: 10 hands      
Player 2: 12 hands

## Test Cases
There is a test case function provided to check various hands.

## Future
Implement a function to check if given input is correct.    
Convert it to a full working game.    
Each player will be shown their win probability at each stage.    
