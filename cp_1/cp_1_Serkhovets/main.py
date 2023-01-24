from collections import Counter
from math import log
import re


def remove_doubles(text):
    text_len = len(text)
    index = 1
    while index != text_len:
        if text[index] == text[index-1]:
            text = text[:index] + text[index+1:]
            text_len -= 1
            continue
        index += 1
    if text[len(text)-1] == text[len(text)-2]:
        text = text[:len(text)-1]
    return text


def filter_text(text):
    text_len = len(text)
    index = 1
    while index != text_len:
        if text[index] not in "абвгдежзийклмнопрстуфхцчшщьюя ":
            text = text[:index] + text[index+1:]
            text_len -= 1
            continue
        index += 1
    return text


def count_entropy(ensamble, base):
    entropy = 0
    for key, val in ensamble.items():
        entropy -= val * log(val, base)
    return entropy


def count_frequencies(text, ngram_size):
    frequencies = None
    sum = 0
    if ngram_size == 1:
        frequencies = dict(Counter(text))
    else:
        frequencies = dict()
        for i in range(0, len(text), ngram_size):
            if len(text[i:]) >= ngram_size:
                if text[i:i+ngram_size] not in frequencies.keys():
                    frequencies[text[i:i + ngram_size]] = 1
                else:
                    frequencies[text[i:i+ngram_size]] += 1
            else:
                ngram = text[i:] + ' ' * (ngram_size-len(text[i:]))
                if ngram not in frequencies.keys():
                    frequencies[ngram] = 1
                else:
                    frequencies[ngram] += 1
    for key, val in frequencies.items():
        sum += val
    for key, val in frequencies.items():
        frequencies[key] = val/sum
    return frequencies


def output_table(ensamble, out_name):
    file = open(out_name, 'wb')
    keys = list(ensamble.keys())
    keys.sort()
    sorted_ensamble = {i: ensamble[i] for i in keys}
    for key, val in sorted_ensamble.items():
        file.write((key + ';' + str(val) + '\n').encode('utf-8'))
    file.close()


def main():
    file = open('plaintext.txt', 'rb')
    unfiltered = file.read().decode('utf-8').lower()
    file.close()
    # plain_spaces_repeat = re.sub('[0-9.,!:;]', '', unfiltered)
    # plain_spaces_repeat = plain_spaces_repeat.replace('\xa0', ' ')
    plain_spaces_repeat = filter_text(unfiltered)
    plain_spaces_repeat = plain_spaces_repeat.replace('  ', ' ')
    plain_no_spaces_repeat = plain_spaces_repeat.replace(' ', '')
    plain_spaces_no_repeat = remove_doubles(plain_spaces_repeat)
    plain_no_spaces_no_repeat = remove_doubles(plain_no_spaces_repeat)

    plain_spaces_repeat_frequencies_monograms = count_frequencies(plain_spaces_repeat, 1)
    plain_no_spaces_repeat_frequencies_monograms = count_frequencies(plain_no_spaces_repeat, 1)
    plain_spaces_repeat_frequencies_bigrams = count_frequencies(plain_spaces_repeat, 2)
    plain_no_spaces_repeat_frequencies_bigrams = count_frequencies(plain_no_spaces_repeat, 2)
    plain_spaces_no_repeat_frequencies_bigrams = count_frequencies(plain_spaces_no_repeat, 2)
    plain_no_spaces_no_repeat_frequencies_bigrams = count_frequencies(plain_no_spaces_no_repeat, 2)

    plain_spaces_repeat_frequencies_monograms_entropy = count_entropy(plain_spaces_repeat_frequencies_monograms, 33)
    plain_no_spaces_repeat_frequencies_monograms_entropy = count_entropy(plain_no_spaces_repeat_frequencies_monograms, 33)
    plain_spaces_repeat_frequencies_bigrams_entropy = count_entropy(plain_spaces_repeat_frequencies_bigrams, 33)
    plain_no_spaces_repeat_frequencies_bigrams_entropy = count_entropy(plain_no_spaces_repeat_frequencies_bigrams, 33)
    plain_spaces_no_repeat_frequencies_bigrams_entropy = count_entropy(plain_spaces_no_repeat_frequencies_bigrams, 33)
    plain_no_spaces_no_repeat_frequencies_bigrams_entropy = count_entropy(plain_no_spaces_no_repeat_frequencies_bigrams, 33)

    print('Ентропія монограм для тексту з пробілами:', plain_spaces_repeat_frequencies_monograms_entropy)
    print('Ентропія монограм для тексту без пробілів:', plain_no_spaces_repeat_frequencies_monograms_entropy)
    print('Ентропія біграм для тексту з пробілами та повторами:', plain_spaces_repeat_frequencies_bigrams_entropy)
    print('Ентропія біграм для тексту без пробілів та з повторами:', plain_no_spaces_repeat_frequencies_bigrams_entropy)
    print('Ентропія біграм для тексту з пробілами та без повторів:', plain_spaces_no_repeat_frequencies_bigrams_entropy)
    print('Ентропія біграм для тексту без пробілів та без повторів:', plain_no_spaces_no_repeat_frequencies_bigrams_entropy)

    output_table(plain_spaces_repeat_frequencies_monograms, 'plain_spaces_repeat_frequencies_monograms.csv')
    output_table(plain_no_spaces_repeat_frequencies_monograms, 'plain_no_spaces_repeat_frequencies_monograms.csv')
    output_table(plain_spaces_repeat_frequencies_bigrams, 'plain_spaces_repeat_frequencies_bigrams_entropy.csv')
    output_table(plain_no_spaces_repeat_frequencies_bigrams, 'plain_no_spaces_repeat_frequencies_bigrams.csv')
    output_table(plain_spaces_no_repeat_frequencies_bigrams, 'plain_spaces_no_repeat_frequencies_bigrams.csv')
    output_table(plain_no_spaces_no_repeat_frequencies_bigrams, 'plain_no_spaces_no_repeat_frequencies_bigrams.csv')


if __name__ == '__main__':
    main()
