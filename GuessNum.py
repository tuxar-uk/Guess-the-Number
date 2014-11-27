#!/usr/bin/python
""" Guess the Number    Copyright (C) Alan Richmond 2014    MIT License.

    This version plays the game for you (so you don't need to)
    using binary search. With a range of 1:128 this should take
    less than log2 128 = 7 guesses. You can experiment by setting
    'binary' to False or True. See
    http://en.wikipedia.org/wiki/Binary_search_algorithm#Number_guessing_game

    I think this is a good introductory didactic program for beginners
    to Python and algorithms. Create a version without the computer making
    its own guesses (i.e. delete the binary search bits) and have students
    play the game and challenge them to find the best strategy (hint:
    how do you search a dictionary or telephone book?)

    It demonstrates very compactly:
    int & boolean data types
    importing libraries
    arithmetic operations: +, -, //
    boolean comparisons: <, >
    simulation with random number generator
    basic input/output
    initialization
    for loop (could also be done with "while not win:")
    conditionals
    binary search
    counter increments and +=
    computer gaming/simulation
    debugging (e.g. make mistakes like put the guess+=1 at end of loop)
"""
binary=False                    # set this to True or False
lonum,hinum=1,128               # range for the number

import random as r

the_num=r.randint(lonum,hinum)  # computer chooses a number randomly
print ("I'm thinking of a number between",lonum,"and",hinum)

lo=1
hi=hinum
guesses=0

for i in range(lonum,hinum):    # repeat this until guess is correct:
                                    # note the int!
#    guess=int(input ("What is your guess: "))
    if binary:  guess=lo+(hi-lo)//2     # integer division
    else:       guess=r.randint(lo,hi)
    print("Guess:",guess)
    guesses+=1                      # add 1 to count of guesses
                                    # check the guessed number
    if guess > the_num:
        print ("Lower!")
        hi=guess                        # bring down the upper bound
    elif guess < the_num:
        print ("Higher!")
        lo=guess                        # push up the lower bound
    else: break                     # yay!

print ("That took",guesses,"guesses")