import random
from math import gcd

min_ = pow(2, 255) + 1
max_ = pow(2, 256) - 1

t2d = lambda x: int(x.encode().hex(), 16)
d2t = lambda x: bytes.fromhex(hex(x)[2:]).decode()

def prime_check(n):
    for i in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251]:
        if n % i == 0:
            return False
    return True


def miller_rabin(n, k=1024):
    round = 0
    s = n - 1
    if not prime_check(n):
        return False
    while s % 2 == 0:
        round += 1
        s //= 2
    for i in range(k):
        a = random.randint(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for j in range(round - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:

            return False
    return True


def rnd():
    p = random.randint(min_, max_)
    while not miller_rabin(p, 256):
        p = random.randint(min_, max_)
    return p


def RSA(p, q):
    n = p * q
    e = random.randint(2, (p - 1) * (q - 1))
    while gcd(e, (p - 1) * (q - 1)) != 1:
        e = random.randint(2, (p - 1) * (q - 1))
    d = pow(e, -1, (p - 1) * (q - 1))
    dct = {}
    dct["public"] = [n, e]
    dct["private"] = [d, p, q]
    return dct


def Encrypt(data, n, e):
    return pow(data, e, n)


def Decrypt(data, d, p, q):
    return pow(data, d, p * q)


def Signature(data, d, p, q):
    return pow(data, d, p * q)


def Verify(data, sign, n, e):
    return pow(sign, e, n) == data


if __name__ == "__main__":
    plaintext = "1488"*5
    R = [rnd() for i in range(4)]
    p = R[0]
    q = R[1]
    p_ = R[2]
    q_ = R[3]

    Alice = RSA(p, q)
    print("Alice keys:",Alice)
    Bob = RSA(p_, q_)
    print("\nBob keys:",Bob)


    print(f"\n\nAlice encrypt message \"{plaintext}\" using Bob public key")
    ciphertext = Encrypt(t2d(plaintext), *Bob["public"])
    print(f"Ciphertext: {ciphertext}")

    print(f"\nAlice create sign for ciphertext using private key")
    sign = Signature(ciphertext, *Alice["private"])
    print(f"Sign: {sign}")


    print("\n\nBob verify sign using Alice public key")
    s = Verify(ciphertext, sign, *Alice["public"])
    print(f"Sign: {s}")
    print("\nBob decrypt Alice ciphertext using private key")
    decoded = d2t(Decrypt(ciphertext, *Bob["private"]))
    print(f"Plaintext: {decoded}")
