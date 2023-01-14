from collections import Counter
from itertools import product
from math import gcd

alphabet = 'абвгдежзийклмнопрстуфхцчшщьыэюя'
impossible = ['еь', 'иь', 'кь', 'ць', 'ыы', 'юь', 'эы', 'еы', 'уь', 'яы', 'аы', 'иы', 'уы', 'яь', 'оы', 'ыь', 'эь', 'юы', 'аь', 'оь', 'хь']
natural = ['ст', 'но', 'то', 'на', 'ен']

n1 = 31
n2 = n1 ** 2

def sliser(txt):
    res = []
    for i in range(0, len(txt), 2):
        res.append(txt[i:i+2])
    return res

def five_bigram(txt):
    c = Counter(sliser(txt)).most_common(5)
    res = []
    for i in c:
        res.append(i[0])
    return res

def bi2int(txt):
    return alphabet.index(txt[0]) * n1 + alphabet.index(txt[1])

def int2bi(num):
    return alphabet[num // n1] + alphabet[num % n1]

def mod_reverse(a, b):
    u_0, u_1 = 1, 0
    while a % b:
        r = a % b
        q = a // b
        a, b = b, r
        u = u_0 - q * u_1
        u_0, u_1 = u_1, u
    return u_1
    # u0, u1 = 1, 0
    # while a % n:
    #     q = a // n
    #     a = n
    #     n = a % n
    #     u0 = u1
    #     u1 = u0 - q * u1
    # return u1

def solve(a, b, n):
    _gcd = gcd(a, n)
    if b % _gcd != 0:
        return []
    if _gcd == 1:
        return [mod_reverse(a, n) * b % n]
    a //= _gcd
    b //= _gcd
    n //= _gcd
    start_x = mod_reverse(a, n) * b % n
    return [start_x + n * i for i in range(_gcd)]

def decrypt(txt, a, b):
    res = ''
    for i in sliser(txt):
        y = bi2int(i)
        x = mod_reverse(a, n2) * (y - b) % n2
        res += int2bi(x)
    return res

def check(text):
    for i in impossible:
        if i in text:
            return False
    return True

with open('22.txt', 'r', encoding='utf-8') as f:
    v22 = f.read().replace('\n', '')

enc_bi = five_bigram(v22)
print(enc_bi)

num_nat = [bi2int(i) for i in natural]
enc_nat = [bi2int(i) for i in enc_bi]
done = False

for x1, y1, x2, y2 in product(num_nat, enc_nat, repeat=2):
    if x1 == x2 or y1 == y2:
        continue
    system = [(i, (y1 - i * x1) % n2) for i in solve(x1 - x2, y1 - y2, n2)]
    for a, b in system:
        d22 = decrypt(v22, a, b)
        if check(d22):
            print('a =', a, 'b =', b)
            print('encrypted\n', v22, '\ndecrypted\n', d22)
            done = True
    if done:
        break