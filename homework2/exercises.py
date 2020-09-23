import re
import math
import pytest
from exercises import (change, stretched, scramble, say, powers,
                       interleave, Cylinder, make_crypto_functions, random_name)


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


def stretched():


def scramble():
    for s in ['a', 'rat', 'JavaScript testing', '', 'zzz', '^*))^*>^▱ÄÈËɡɳɷ']:
        assert sorted(s) == sorted(scramble(s))
    possibilities = set(['ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA'])
    for _ in range(200):
        possibilities.discard(scramble('ABC'))
    assert not possibilities


def cylinder():
    c = Cylinder(radius=10, height=5)
    assert c.height == 5
    assert c.radius == 10
    c = Cylinder(height=5)
    assert c.height == 5
    assert c.radius == 1
    c = Cylinder(radius=5)
    assert c.height == 1
    assert c.radius == 5
    c = Cylinder()
    assert c.height == 1
    assert c.radius == 1
    c = Cylinder(radius=2, height=10)
    assert pytest.approx(c.volume, 0.000001) == 40 * math.pi
    assert pytest.approx(c.surface_area, 0.000001) == 48 * math.pi
    c.widen(3)
    assert c.radius == 6
    c.stretch(2)
    assert c.height == 20
    assert pytest.approx(c.surface_area, 0.000001) == 312 * math.pi
    assert pytest.approx(c.volume, 0.000001) == 720 * math.pi


def powers():
    p = powers(2, 10)
    assert next(p) == 1
    assert next(p) == 2
    assert next(p) == 4
    assert next(p) == 8
    with pytest.raises(StopIteration):
        next(p)
    assert list(powers(2, -5)) == []
    assert list(powers(7, 0)) == []
    assert list(powers(3, 1)) == [1]
    assert list(powers(2, 63)) == [1, 2, 4, 8, 16, 32]
    assert list(powers(2, 64)) == [1, 2, 4, 8, 16, 32, 64]


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