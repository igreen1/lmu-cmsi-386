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



class cylinder():

    radius = 1
    height = 1

    def __init__(self, r, h):
        self.radius = r
        self.height = h

    def volume():
        return self.height * math.pi * (self.radius ** 2)

    def surface_area():
        return (2 * math.pi * self.radius * self.height) + (2 * math.pi * (self.radius ** 2))

    def widen(factor):
        self.radius = self.radius * factor

    def stretch(factor):
        self.height = self.height * factor

'''

A function that yields successive powers of a base starting at the 0th power, namely 1, and going up to some limit. Consume the values with a callback. 


'''

def powers(base, limit):
    current_value = 1
    while current_value <= limit:
        yield current_value
        current_value = current_value*base


'''

A “chainable” function that accepts one string per call, but when called without arguments, returns the words previously passed, in order, separated by a single space


'''

def say(input=None):
    if input is None:
        return ""
    else:


'''

A function that interleaves an array with a bunch of values. If the array length is not the same as the number of values to interleave, the “extra” elements should end up at the end of the result. 


'''

def interleave():

'''

A function that accepts three arguments: a crypto key, a crypto algorithm, and an initialization vector, and returns an array of two functions. The first returned function is an encryption function that encrypts a string into a hex string, and the second is a decryption function that decrypts the hex string into a string. Use the functions createCipheriv and createDecipheriv from the built-in Node crypto module. 

'''

def crypto():

'''

A function that returns the top ten players by points-per-game among the players that have been in 15 games or more. The input to your function will be an object, keyed by team, with a list of player stats. Each player stat is an array with the player name, the number of games played, and the total number of points, for example: 

'''

def top_ten_scorers():


def random_name():

























