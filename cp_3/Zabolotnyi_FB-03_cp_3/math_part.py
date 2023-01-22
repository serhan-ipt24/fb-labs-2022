from numpy import gcd


def euclid_extend(a, b):
    if a == 0:
        return b, 0, 1
    gcd_, m, n = euclid_extend(b % a, a)
    x = n - ((b // a) * m)
    y = m
    return gcd_, x, y


def linear_cmp(a, b, mod):
    d = gcd(a, mod)
    if d == 1:
        return [(euclid_extend(a, mod)[1] * b) % mod]
    elif d > 1:
        if b % d != 0:
            return None
        else:
            result = []
            x0 = (euclid_extend(a // d, mod // d)[1] * b // d) % mod // d
            for i in range(d):
                result.append(x0 + ((mod % d) * i))
            return result
