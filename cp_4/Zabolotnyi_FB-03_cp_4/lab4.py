import random
from numpy import gcd
import pandas as pd


def random_number(start, finish):
    def miller_rabin(number):
        if number % 2 == 0 or number % 3 == 0 or number % 5 == 0 or number % 7 == 0 or number % 11 == 0 or number % 13 == 0:
            return False
        d, s = number - 1, 0
        while True:
            if d % 2 == 0:
                break
            d = d // 2
            s += 1
        rand = random.randint(2, number - 2)
        if gcd(rand, number) > 1:
            return False
        elif pow(rand, d, number) == 1 or pow(rand, d, number) == -1:
            return True
        else:
            for i in range(1, s - 1):
                rand = pow(rand, 2, number)
                if rand == - 1:
                    return True
                if rand == 1:
                    return False
            return False

    while True:
        number = random.randint(start, finish)
        if miller_rabin(number) is True:
            return number


while True:
    sender = (random_number(2 ** 256, 2 ** 260), random_number(2 ** 256, 2 ** 260))
    recipient = (random_number(2 ** 256, 2 ** 260), random_number(2 ** 256, 2 ** 260))
    if sender[0] * sender[1] > recipient[0] * recipient[1]:
        break


def gen_keys(p, q):
    n = p * q
    f = (p - 1) * (q - 1)
    e = 2 ** 16 + 1
    d = pow(e, -1, f)
    open = (e, n)
    close = (p, q, d)
    return open, close


sender_open, sender_close = gen_keys(sender[0], sender[1])
recipient_open, recipient_close = gen_keys(recipient[0], recipient[1])
message = random.randint(2 ** 256, 2 ** 260)


def encryption(message, sender_ok):
    encrypted_message = pow(message, sender_ok[0], sender_ok[1])
    return encrypted_message


encrypted_message = encryption(message, recipient_open)


def signature_creation(message, sender_ck):
    signature = pow(message, sender_ck[2], sender_ck[0] * sender_ck[1])
    return signature


signature = signature_creation(message, sender_close)
encrypted_signature = encryption(signature, recipient_open)


def decryption(message, recipient_ok):
    decrypted_message = pow(message, recipient_ok[2], recipient_ok[0] * recipient_ok[1])
    return decrypted_message


decrypted_message = decryption(encrypted_message, recipient_close)
decrypted_signature = decryption(encrypted_signature, recipient_close)

data = {"Sender open key": sender_open, "Sender close key": sender_close, "Recipient open key": recipient_open,
        "Recipient close key": recipient_close, "Message": message, "Encrypted message": encrypted_message,
        "Sender signature": signature, "Encrypted signature": encrypted_signature,
        "Decrypted message": decrypted_message, "Decrypted signature": decrypted_signature}
df = pd.Series(data)
print(df)
df.to_excel("values.xlsx")


def check_sign(decrypted_message, signature, sender_ok):
    if pow(signature, sender_ok[0], sender_ok[1]) == decrypted_message:
        print("Good signature")
    else:
        print("Bad signature")


print('')
check_sign(decrypted_message, decrypted_signature, sender_open)
