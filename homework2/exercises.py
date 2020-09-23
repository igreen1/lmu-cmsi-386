import re
import math
import pytest
import random
from exercises import (change, stretched, scramble, say, powers,
                       interleave, Cylinder, make_crypto_functions, random_name)

'''

A function that accepts a number of U.S. cents and returns an 
    array containing, respectively, the smallest number of U.S. 
    quarters, dimes, nickels, and pennies that equal the given amount. 
Input: # of US cents 
Return [quarters, dimes, nickels, pennies]

'''
def change(total_cents):
    if total_cents < 0:
        raise Exception("Sorry, the total number of cents must be greater than or equal to zero.")
    
    coin_values = (25,10,5,1) # unchangeable tuple: stores the values of the denominations in decreasing order
    coins_used = [0,0,0,0] # stores how many of each respective denomination was used
    remaining_cents = total_cents # holds the amount of cents we still need to make change for
    temp = 0
    
    for i in range( len(coin_values) ):
        temp = math.floor(remaining_cents/coin_values[i]) # holds the amount of this denom we can use
        remaining_cents = remaining_cents - temp * coin_values[i] # remove the cents since we have now 'given' change for that amount
        coins_used[i] = temp # store how much 'change' we have used

    return tuple(coins_used)

'''

A function that accepts a string and returns a new string equal to the initial string with all 
    whitespace removed and then with the ith character (1-based) repeated i times. 
Input: string 
Output: input string with no white space and repeated characters based on position

'''
def stretched(input):
    output = ""
    for i in range len(input):
        if input[i] != " ":
            output = output + input[i]

    for i in range(len(input) - len(output)):
        output = output + output[i]

    return output

'''

A function that randomly permutes a string. What does random mean? It means that each time you 
    call the function for a given argument, all possible permutations are equally likely. 
    Random is not the same as arbitrary. 
Input: string
Output: input string permuted randomly

'''

def scramble(input):
    if len(input) <= 0:
        return input
    
    output = ""
    while len(input) > 0:
        i = math.floor(random.random() * len(input))
        output = output + input[i]
        input = input[:i] + input[i + 1:]

    return output



def cylinder():

'''

A function that yields successive powers of a base starting at the 0th power, namely 1, and going up to some limit. Consume the values with a callback. 


'''

def powers(base, limit, callback):



def say():


def interleave():


def crypto():


def top_ten_scorers():


def random_name():
