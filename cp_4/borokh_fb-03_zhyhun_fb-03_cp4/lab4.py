from random import randint
from numpy import gcd


def miller_rabin_test(num):
    if num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0 or num % 11 == 0 or num % 13 == 0:
        return False

    d = num - 1
    s = 0
    while d % 2 == 0:
        d = d // 2
        s += 1

    x = randint(2, num - 2)

    if gcd(x, num) > 1:
        return False

    if pow(x, d, num) == 1 or pow(x, d, num) == -1:
        return True

    for i in range(1, s - 1):
        x = (x ** 2) % num
        if x == - 1:
            return True
        if x == 1:
            return False
    return False


def random_search(n_max, n_min=0):
    while True:
        x = randint(n_min, n_max)
        if miller_rabin_test(x):
            return x


def create_keys(p, q):
    e = 2 ** 16 + 1
    n = p * q
    fi = (p - 1) * (q - 1)

    d = pow(e, -1, fi)

    open_key = (n, e)
    secret_key = (d, p, q)

    return open_key, secret_key


def encryption(data, open_key_B):
    return pow(data, open_key_B[1], open_key_B[0])


def decryption(data, secret_key_B):
    return pow(data, secret_key_B[0], secret_key_B[2] * secret_key_B[1])


def make_signature(data, secret_key_A):
    return pow(data, secret_key_A[0], secret_key_A[2] * secret_key_A[1])


def authentication(de_data, de_signed, open_key_A):
    if de_data == pow(de_signed, open_key_A[1], open_key_A[0]):
        return True
    return False


if __name__ == "__main__":
    # random prime nums
    A_numbers = (random_search(2 ** 258, 2 ** 256), random_search(2 ** 258, 2 ** 256))
    B_numbers = (random_search(2 ** 258, 2 ** 256), random_search(2 ** 258, 2 ** 256))

    if A_numbers[0] * A_numbers[1] > B_numbers[0] * B_numbers[1]:
        A_numbers, B_numbers = B_numbers, A_numbers

    # keys
    open_A, secret_A = create_keys(A_numbers[0], A_numbers[1])
    open_B, secret_B = create_keys(B_numbers[0], B_numbers[1])

    print(f"\nA side open key:\n{open_A}")
    print(f"\nA side secret key:\n{secret_A}")

    print(f"\nB side open key:\n{open_B}")
    print(f"\nB side secret key:\n{secret_B}")

    message = randint(2 ** 100, 2 ** 200)

    print(f"\nOpen message: {message}")

    # message encryption
    encrypted = encryption(message, open_B)
    print(f"\nEncrypted message: {encrypted}")
    # signature creation
    signed = make_signature(message, secret_A)
    print(f"\nSignature: {signed}")
    # signature encryption
    en_signed = encryption(signed, open_B)
    print(f"\nEncrypted signature: {en_signed}")

    # ...
    # sending encrypted data
    # ...

    # data decryption
    decrypted = decryption(encrypted, secret_B)
    print(f"\nDecrypted message: {decrypted}")
    # signature description
    de_signed = decryption(en_signed, secret_B)
    print(f"\nDecrypted signature: {de_signed}")

    # verification
    print("\n Verification ^-^\n")
    if authentication(decrypted, de_signed, open_A):
        print("Authenticated successfully!")
    else:
        print("Wrong signature!!!")
