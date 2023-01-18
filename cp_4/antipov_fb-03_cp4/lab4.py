import random


def my_gcd(a, b):
    if b == 0:
        return abs(a)
    else:
        return my_gcd(b, a % b)


def simple_test(number):
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for prime_number in prime_numbers:
        if number % prime_number == 0:
            return False
        else:
            return True


def miller_rabin(number, q=150):
    if simple_test(number) is False:
        return False
    else:
        s = 0
        d = number - 1

        while d % 2 == 0:
            d //= 2
            s += 1

        for j in range(q):
            x = random.randint(2, number - 1)
            g = my_gcd(x, number)
            if g > 1:
                return False
            if g == 1:
                if pow(x, d, number) in [-1, 1]:
                    return True
                else:
                    for r in range(1, s - 1):
                        if pow(x, d * pow(2, r), number) == 1:
                            return False
                        elif pow(x, d * pow(2, r), number) == -1:
                            return True
            else:
                return False


def generate_prime_number(length):
    while True:
        rand = random.randrange(2 ** (length - 1), 2 ** length)
        if miller_rabin(rand):
            return rand


def generate_pairs():
    p = generate_prime_number(256)
    q = generate_prime_number(256)
    p1 = generate_prime_number(256)
    q1 = generate_prime_number(256)
    if (p * q) <= (p1 * q1):
        return [p, q, p1, q1]


def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
    return [gcd, y - (b // a) * x, x]


def inverse(a, b):
    if a < 0:
        a += b
    gcd, x, y = extended_gcd(a, b)
    if gcd == 1:
        return x
    else:
        return 0


def rsa_combinations(p, q):
    n = p * q
    fi = (p - 1) * (q - 1)
    e = random.randrange(2, fi - 1)
    while my_gcd(e, fi) != 1:
        e = random.randrange(2, fi -1)
    d = pow(e, -1, fi)
    print(fi)
    return [e, n, d]


def show_keys():
    pairs = generate_pairs()
    p, q, p1, q1 = pairs[0], pairs[1], pairs[2], pairs[3]
    keys_for_a = rsa_combinations(p, q)
    keys_for_b = rsa_combinations(p1, q1)
    e, n, d = keys_for_a[0], keys_for_a[1], keys_for_a[2]
    e1, n1, d1 = keys_for_b[0], keys_for_b[1], keys_for_b[2]
    print('Ключі для абонента A:')
    print('d:', d)
    print('p:', p)
    print('q:', q)
    print('n:', n)
    print('e:', e)
    print('Ключі для абонента B:')
    print('d:', d1)
    print('p:', p1)
    print('q:', q1)
    print('n:', n1)
    print('e:', e1)


show_keys()
