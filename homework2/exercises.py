import re
import math
import pytest
import random
from cryptography.fernet import Fernet
import requests
import json

'''

A function that accepts a number of U.S. cents and returns an
    array containing, respectively, the smallest number of U.S.
    quarters, dimes, nickels, and pennies that equal the given amount.
Input: # of US cents
Return [quarters, dimes, nickels, pennies]

'''


def change(total_cents):
    if total_cents < 0:
        raise ValueError(
            "amount cannot be negative")

    denominations = (25, 10, 5, 1)
    denominations_used = []
    remaining_cents = total_cents

    for denomination in denominations:
        denominations_used.append(math.floor(remaining_cents / denomination))
        remaining_cents %= denomination

    return tuple(denominations_used)


'''

A function that accepts a string and returns a new string equal to the initial string with all
    whitespace removed and then with the ith character (1-based) repeated i times.
Input: string
Output: input string with no white space and repeated characters based on position

'''


def stretched(s):  # CHECK SLACK- Toal had bug with emojis he might want fixed for this
    s = "".join(s.split())
    stretched = ""

    for i in range(0, len(s)):
        stretched += s[i] * (i + 1)

    return stretched


'''

A function that randomly permutes a string. What does random mean? It means that each time you
    call the function for a given argument, all possible permutations are equally likely.
    Random is not the same as arbitrary.
Input: string
Output: input string permuted randomly

'''


def scramble(s):
    scrambled = ""

    while len(s) > 0:
        i = math.floor(random.random() * len(s))
        scrambled += s[i]
        s = s[:i] + s[i + 1:]

    return scrambled


'''

A traditional Python Cylinder class. The initializer should accept a radius and height as keyword arguments;
both should default to 1 if not passed in. Include volume and surface area methods exposed as properties,
as well as a widen method that mutates the radius by a given factor and a stretch method to grow the height.

'''


class Cylinder():
    def __init__(self, radius=1, height=1):
        self.radius = radius
        self.height = height

    @property
    def volume(self):
        return self.height * math.pi * (self.radius ** 2)

    @property
    def surface_area(self):
        return (2 * math.pi * self.radius * self.height) + \
            (2 * math.pi * (self.radius ** 2))

    def widen(self, factor):
        self.radius *= factor

    def stretch(self, factor):
        self.height *= factor


'''

A function that yields successive powers of a base starting at the 0th power, namely 1, and going up to some limit. Consume the values with a callback.


'''


def powers(base, limit):
    power = 1
    while power <= limit:
        yield power
        power *= base


'''

A “chainable” function that accepts one string per call, but when called without arguments,
returns the words previously passed, in order, separated by a single space.


'''


def say(first=None):
    if first == None:
        return ""

    def join_with_space(second=None):
        if second == None:
            return first
        return say(first + " " + second)

    return join_with_space


'''

A function that interleaves a list with a bunch of values. If the list length is not the same
as the number of values to interleave, the “extra” elements should end up at the end of the result.


'''


def interleave(a, *b):
    minimum_length = min(len(a), len(b))
    interwoven = []

    for i in range(0, minimum_length):
        interwoven.append(a[i])
        interwoven.append(b[i])

    return interwoven + a[minimum_length:] + list(b[minimum_length:])


'''

A function that accepts a Fernet key and returns a tuple of two functions. The first function encrypts a
bytes object with the key. The second decrypts. Both functions accept a bytes object and return a bytes object.
Use the cryptography package. You are responsible for reading the documentation for the package;
we are not going over this in class.

'''


def make_crypto_functions(key):
    def encryption(to_encrypt):
        return Fernet(key).encrypt(to_encrypt)

    def decryption(to_decrypt):
        return Fernet(key).decrypt(to_decrypt)

    return(encryption, decryption)


'''

A function that returns the top ten players by points-per-game among the players that have been in 15 games or more.
The input to your function will be a dictionary, keyed by team, with a list of player stats. Each player stat is a list
with the player name, the number of games played, and the total number of points, exactly as in Homework 1.

'''


def top_ten_scorers(stats):
    return sorted([{'name': name,
                    'ppg': points / game,
                    'team': team} for team,
                   players in stats.items() for name,
                   game,
                   points in players if game >= 15],
                  key=lambda scorer: scorer['ppg'],
                  reverse=True)[:10]


'''

A function that returns a list of people from the Studio Ghibli API. This function should use the requests module
and you are to fetch the data synchronously. Require exactly two search parameters hair_color and gender and require
that they be passed as kwargs. Your function should return the list of people from the API search as dictionaries
with the keys name, gender, age, eye_color, and hair_color.

'''


def studio_ghibli_characters(*, hair_color, gender):
    characters = json.loads(requests.get(
        "https://ghibliapi.herokuapp.com/people").text)
    return [{'name': character['name'], 'gender': character['gender'], 'age': character['age'], 'eye_color': character['eye_color'],
             'hair_color': character['hair_color']} for character in characters if character['hair_color'] == hair_color and character['gender'] == gender]
