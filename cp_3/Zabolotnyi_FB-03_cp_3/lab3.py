from math_part import linear_cmp, euclid_extend

text = open('10.txt', 'r', encoding='UTF-8').read().replace('\n', '')


bi_dict = {}
for i in range(0, len(text), 2):
    j = i + 2
    if len(text[i:j]) == 1:
        continue
    if text[i:j] in bi_dict.keys():
        bi_dict[text[i:j]] += 1
    else:
        bi_dict[text[i:j]] = 1
result = zip(bi_dict.keys(), bi_dict.values())
result = sorted(result, key=lambda x: x[1], reverse=True)[:5]
founded_bi = [i[0] for i in result]
static_bi = ("ст", "но", "то", "на", "ен")


def make_variants(bi1, bi2):
    variants = []
    for i in bi1:
        for j in bi2:
            variants.append((j, i))
    result = []
    for i in variants:
        for j in variants:
            if (i != j) and ((j, i) not in result) and (i[0] != j[0]) and (i[1] != j[1]):
                result.append((i, j))
    return result


def bi_to_num(biagram):
    alphabet = 'абвгдежзийклмнопрстуфхцчшщьыэюя'
    return alphabet.find(biagram[0]) * 31 + alphabet.find(biagram[1])


def found_keys(static, encoded):
    x = bi_to_num(static[0]) - bi_to_num(static[1])
    y = bi_to_num(encoded[0]) - bi_to_num(encoded[1])
    keys = linear_cmp(x, y, 31 ** 2)
    result = []
    if keys is not None:
        if len(keys) > 0:
            for key in keys:
                result.append((key, (bi_to_num(encoded[0]) - key * bi_to_num(static[0])) % (31 ** 2)))
        return result


keys = []
possible = make_variants(founded_bi, static_bi)
for i in possible:
    answer_keys = found_keys((i[0][0], i[1][0]), (i[0][1], i[1][1]))
    if answer_keys is None:
        continue
    for k in answer_keys:
        keys.append(k)


def num_to_bi(number):
    alphabet = 'абвгдежзийклмнопрстуфхцчшщьыэюя'
    return alphabet[number // 31] + alphabet[number % 31]


def decrypt_text(text, key):
    result = []
    for i in range(0, len(text), 2):
        if i >= len(text):
            break
        y = bi_to_num(text[i: i + 2])
        x = (euclid_extend(key[0], 31 ** 2)[1] * (y - key[1])) % (31 ** 2)
        result.append(num_to_bi(x))
    return ''.join(result)


def error_check(text):
    bad_bi = ['аы', 'еы', 'уы', 'еь', 'эы', 'яь', 'ьь', 'ыь', 'эь', 'уь', 'оь', 'ыы', 'оы', 'юь', 'юы', 'яы']
    for bi in bad_bi:
        if bi in text:
            return False
    return True

key = None
test = None
for key in keys:
    test = decrypt_text(text, key)
    if error_check(test):
        break
print("Decrypted by:", key, "\nResult:", test)

open('result.txt', 'w').write(test)
