from math import gcd
from collections import Counter
alphabet = "абвгдежзийклмнопрстуфхцчшщьыэюя"

with open('1.txt', 'r', encoding='utf-8') as file:
    my_text = file.read().replace('\n', '')


def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
    return gcd, y - (b // a) * x, x


def inverse(a, b):
    gcd, x, y = extended_gcd(a, b)
    if gcd == 1:
        return x % b
    else:
        return 0


def solve_equation(a, b, m):
    d = gcd(a, m)
    if d == 1:
        ans = (inverse(a, m) * b) % m
    elif (b % d) != 0:
        ans = 0
    else:
        ans = solve_equation(a // d, b // d, m // d)
    return ans


def find_top_bigrams(text):
    bigrams = []
    for i in range(0, len(text), 2):
        bigrams.append(text[i:i + 2])
    return sorted(dict(Counter(bigrams)), key=dict(Counter(bigrams)).get, reverse=True)[:5]


def bigrams_to_int(bigrams):
    return [alphabet.index(i[0]) * len(alphabet) + alphabet.index(i[1]) for i in bigrams]


print(find_top_bigrams(my_text))
print(bigrams_to_int(find_top_bigrams(my_text)))
