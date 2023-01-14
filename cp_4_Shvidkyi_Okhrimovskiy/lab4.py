from random import getrandbits, randint
from math import gcd

def reverse(a, n):
    return pow(a, -1, n)

def miller_rabin(p):
    for i in (2, 3, 5, 7, 11):
        if p == i:
            return True
        if p % i == 0:
            return False
    k = 17
    d = p - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for i in range(k):
        x = randint(2, p-1)
        if gcd(x, p) > 2:
            return False
        if pow(x, d, p) in (1, -1 % p):
            continue
        xi = pow(x, 2, p)
        for i in range(s-1):
            xi = pow(xi, 2, p)        
            if xi == p - 1:
                break
            if xi == 1:
                return False
        else:
            return False
    return True

def get_simple():
    with open('numbers.txt', 'w', encoding='utf-8') as f:
        p = getrandbits(256)
        while not miller_rabin(p):
            f.write(str(hex(p)) + '\n')
            p = getrandbits(256)
        q = getrandbits(256)
        while not miller_rabin(q):
            f.write(str(hex(q)) + '\n')
            q = getrandbits(256)
    return p, q

def GenerateKeyPair():
    p, q = get_simple()
    oiler = (p - 1) * (q - 1)
    e = 2 ** 16 + 1
    n = p * q
    d = reverse(e, oiler)
    return (n, e), (d, p, q)

def Encrypt(msg, e, n):
    return pow(msg, e, n)

def Decrypt(c, d, n) -> int:
    return pow(c, d, n)

def Sign(msg, d, n):
    return msg, pow(msg, d, n)

def Verify(msg, sign, e, n):
    return msg == pow(sign, e, n)

def SendKey(k, d, n, e1, n1):
    S = pow(k, d, n)
    S1 = pow(S, e1, n1)
    k1 = pow(k, e1, n1)
    return k1, S1, S

def ReceiveKey(k1, S1, d1, n1, e, n):
    k = pow(k1, d1, n1)
    S = pow(S1, d1, n1)
    return k, S

(n1, e1), (d1, p1, q1) = GenerateKeyPair()
(n2, e2), (d2, p2, q2) = GenerateKeyPair()

msg = 4444444444444444444444
c1 = Encrypt(msg, e1, n1)
c2 = Encrypt(msg, e2, n2)
s1 = Sign(msg, d1, n1)
s2 = Sign(msg, d2, n2)
k = 999999999999999999999999
if n2 >= n1:
    k1, S1, S = SendKey(k, d1, n1, e2, n2)
    kk, SS = ReceiveKey(k1, S1, d2, n2, e1, n1)
else:
    k1, S1, S = SendKey(k, d2, n2, e1, n1)
    kk, SS = ReceiveKey(k1, S1, d1, n1, e2, n2)

txt = f"""
n1 = {n1}
e1 = {e1}
d1 = {d1}
p1 = {p1}
q1 = {q1}

n2 = {n2}
e2 = {e2}
d2 = {d2}
p2 = {p2}
q2 = {q2}

msg = {msg}
c1 = {c1}
c2 = {c2}
d1 = {Decrypt(c1, d1, n1)}
d2 = {Decrypt(c2, d2, n2)}

s1 = {s1}
s2 = {s2}
v1 = {Verify(s1[0], s1[1], e1, n1)}
v2 = {Verify(s2[0], s2[1], e2, n2)}

k = {k}
S = {S}
S1 = {S1}
k1 = {k1}
k = {kk}
S = {SS}
"""

with open("res.txt", 'w', encoding='utf-8') as f:
    f.write(txt)