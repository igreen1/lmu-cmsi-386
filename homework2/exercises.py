import re
import math
import pytest
import random
from cryptography.fernet import Fernet

'''

A function that accepts a number of U.S. cents and returns an 
    array containing, respectively, the smallest number of U.S. 
    quarters, dimes, nickels, and pennies that equal the given amount. 
Input: # of US cents 
Return [quarters, dimes, nickels, pennies]

'''


def change(total_cents):  # watch his javascript solution from class to fix names & update solution
    if total_cents < 0:
        raise ValueError(
            "amount cannot be negative")

    denominations = (25, 10, 5, 1)
    denominations_used = [0, 0, 0, 0]
    remaining_cents = total_cents
    denominationUses = 0  # HE WILL TAKE OFF POINTS FOR NAMES LIKE "TEMP"

    for i in range(len(denominations)):
        denominationUses = math.floor(remaining_cents/denominations[i])
        remaining_cents = remaining_cents - denominationUses * denominations[i]
        denominations_used[i] = denominationUses

    return tuple(denominations_used)


'''

A function that accepts a string and returns a new string equal to the initial string with all 
    whitespace removed and then with the ith character (1-based) repeated i times. 
Input: string 
Output: input string with no white space and repeated characters based on position

'''


def stretched(input):
    input = "".join(input.split())
    output = ""

    for i in range(0, len(input)):
        output += input[i]*(i+1)

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


'''

A traditional Python Cylinder class. The initializer should accept a radius and height as keyword arguments;
both should default to 1 if not passed in. Include volume and surface area methods exposed as properties,
as well as a widen method that mutates the radius by a given factor and a stretch method to grow the height.

'''


class Cylinder():

    radius = 1
    height = 1

    def __init__(self, radius=1, height=1):
        self.radius = radius
        self.height = height

    def volume(self):
        return self.height * math.pi * (self.radius ** 2)

    def surface_area(self):
        return (2 * math.pi * self.radius * self.height) + (2 * math.pi * (self.radius ** 2))

    def widen(self, factor):
        self.radius = self.radius * factor

    def stretch(self, factor):
        self.height = self.height * factor


'''

A function that yields successive powers of a base starting at the 0th power, namely 1, and going up to some limit. Consume the values with a callback. 


'''


def powers(base, limit):
    power = 1
    while power <= limit:
        yield power
        power = power*base


'''

A “chainable” function that accepts one string per call, but when called without arguments,
returns the words previously passed, in order, separated by a single space.


'''


def say(input=None):
    if input is None:
        return ""
    else:
        def connectStrings(nextInput=None):
            if nextInput is None:
                return input
            else:
                return say(input + " " + nextInput)
        return connectStrings


'''

A function that interleaves an list with a bunch of values. If the list length is not the same
as the number of values to interleave, the “extra” elements should end up at the end of the result.


'''


def interleave(toInterleave, *values):
    interwoven = []
    length1 = len(toInterleave)
    length2 = len(values)

    for i in range(max(length1, length2)):
        if i < length1:
            interwoven.append(toInterleave[i])
        if i < length2:
            interwoven.append(values[i])

    return interwoven


'''

A function that accepts a Fernet key and returns a tuple of two functions. The first function encrypts a
bytes object with the key. The second decrypts. Both functions accept a bytes object and return a bytes object.
Use the cryptography package. You are responsible for reading the documentation for the package;
we are not going over this in class.

'''


def make_crypto_functions(key):
    def encryption(toEncrypt):
        return Fernet(key).encrypt(toEncrypt)

    def decryption(toDecrypt):
        return Fernet(key).decrypt(toDecrypt)
    return(encryption, decryption)


'''

A function that returns the top ten players by points-per-game among the players that have been in 15 games or more.
The input to your function will be a dictionary, keyed by team, with a list of player stats. Each player stat is a list
with the player name, the number of games played, and the total number of points, exactly as in Homework 1.

'''


def top_ten_scorers(teamsAndPlayers):
    return


'''

A function that returns a list of people from the Studio Ghibli API. This function should use the requests module and you are to fetch the data synchronously. Require exactly two search parameters hair_color and gender and require that they be passed as kwargs. Your function should return the list of people from the API search as dictionaries with the keys name, gender, age, eye_color, and hair_color.

'''


def studio_ghibli_characters(hair_color="", gender=""):
    return
