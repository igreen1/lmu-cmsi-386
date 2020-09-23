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
    assert say() == ''
    assert say('hi')() == 'hi'
    assert say('hi')('there')() == 'hi there'
    assert say('hello')('my')('name')('is')(
        'Colette')() == 'hello my name is Colette'


def interleave():
    assert interleave([]) == []
    assert interleave([1, 4, 6]) == [1, 4, 6]
    assert interleave([], 2, 3) == [2, 3]
    assert interleave([1], 9) == [1, 9]
    assert interleave([8, 8, 3, 9], 1) == [8, 1, 8, 3, 9]
    assert interleave([2], 7, '8', {}) == [2, 7, '8', {}]
    a = [1, 2, 3, 4]
    assert interleave(a, 10, 20, 30) == [1, 10, 2, 20, 3, 30, 4]
    # Test input list not destroyed
    assert a == [1, 2, 3, 4]


def crypto():
    assert isinstance(make_crypto_functions(
        b"A2qK5XG3qX1MfLrGacD9AGVG2sbZYkvFFki94qbkVhE="), tuple)
    e, d = make_crypto_functions(
        b"A2qK5XG3qX1MfLrGacD9AGVG2sbZYkvFFki94qbkVhE=")
    for s in [b'', b'\xfe9iP\x05\x22\x490opXZ@1##', b'Helllllllllooooooo world']:
        assert d(e(s)) == s


def top_ten_scorers():
    stats = {
        'ATL': [
            ['Betnijah Laney', 16, 263],
            ['Courtney Williams', 14, 193],
        ],
        'CHI': [
            ['Kahleah Copper', 17, 267],
            ['Allie Quigley', 17, 260],
            ['Courtney Vandersloot', 17, 225],
        ],
        'CONN': [
            ['DeWanna Bonner', 16, 285],
            ['Alyssa Thomas', 16, 241],
        ],
        'DAL': [
            ['Arike Ogunbowale', 16, 352],
            ['Satou Sabally', 12, 153],
        ],
        'IND': [
            ['Kelsey Mitchell', 16, 280],
            ['Tiffany Mitchell', 13, 172],
            ['Candice Dupree', 16, 202],
        ],
        'LA': [
            ['Nneka Ogwumike', 14, 172],
            ['Chelsea Gray', 16, 224],
            ['Candace Parker', 16, 211],
        ],
        'LV': [
            ['A’ja Wilson', 15, 304],
            ['Dearica Hamby', 15, 188],
            ['Angel McCoughtry', 15, 220],
        ],
        'MIN': [
            ['Napheesa Collier', 16, 262],
            ['Crystal Dangerfield', 16, 254],
        ],
        'NY': [
            ['Layshia Clarendon', 15, 188]
        ],
        'PHX': [
            ['Diana Taurasi', 13, 236],
            ['Brittney Griner', 12, 212],
            ['Skylar Diggins-Smith', 16, 261],
            ['Bria Hartley', 13, 190],
        ],
        'SEA': [
            ['Breanna Stewart', 16, 317],
            ['Jewell Loyd', 16, 223],
        ],
        'WSH': [
            ['Emma Meesseman', 13, 158],
            ['Ariel Atkins', 15, 212],
            ['Myisha Hines-Allen', 15, 236],
        ],
    }
    assert stats


def random_name():
    pass
    # p = random_name(gender='female', region='canada')
    # assert isinstance(p, str)
    # assert len(p) > 3
    # assert ', ' in p
    # with pytest.raises(ValueError) as excinfo:
    #     random_name(gender='fjweiuw', region='canada')
    # assert re.match(r'{"error":\s*"Invalid gender"}', str(excinfo.value))