with open('text.txt', 'r', encoding="UTF-8") as file:
    open_text = file.read().replace('\n', '')
    open_text = open_text.lower()
    open_text = open_text.replace(' ', '')
    open_text = open_text.replace("ё", "е")
    open_text = open_text.replace("ъ", "ь")

keys = ['зд', 'здр', 'здра', 'здрав', 'здравствуймир']

letters_set = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
encrypted_texts = {}

for i in keys:  # шифрування тексту різними ключами
    result = ''
    for j in range(len(open_text)):
        letter = (letters_set.find(open_text[j]) + (letters_set.find(i[j % len(i)]))) % len(letters_set)
        result += letters_set[letter]
    encrypted_texts[i] = result


# print(encrypted_texts)


def freq(text):
    nums = []
    for i in letters_set:
        num = 0
        for j in text:
            if i == j:
                num += 1
        nums.append((i, num))
    return sorted(nums, key=lambda x: x[1], reverse=True)


amount = []
for text in encrypted_texts.values():  # обрахунок кількості букв у кожному ШТ
    nums = freq(text)
    amount.append(nums)


def calc_ind(text, letters):
    index = 0
    for i in range(len(letters)):
        index += letters[i][1] * (letters[i][1] - 1)
    return (1 / (len(text) * (len(text) - 1))) * index


indexes = []
for len_text in range(len(encrypted_texts.values())):  # обрахунок індексів відповідності для ШТ
    indexes.append(calc_ind(list(encrypted_texts.values())[len_text], amount[len_text]))
print(indexes)

with open('text10.txt', 'r', encoding='UTF-8') as file:
    text = file.read().replace('\n', '')

search_ind = []
search_arr = []
for i in range(2, 30):
    itter = []
    for j in range(0, len(text) - i, i):
        for k in range(i):
            if len(itter) > k:
                itter[k] += text[j + k]
            else:
                itter.append(text[j + k])
    search_arr.append(itter)
    buf = []
    for j in itter:
        buf.append(calc_ind(j, freq(j)))
    search_ind.append(sum(buf) / i)

with open('ostin_gordost-i-predubezhdenie_yu17og_308252.txt', 'r', encoding='UTF-8') as file:
    lab1_text = file.read().replace('\n', '')
    lab1_text = lab1_text.lower()
    lab1_text = lab1_text.replace(' ', '')
    lab1_text = lab1_text.replace("ё", "е")
    lab1_text = lab1_text.replace("ъ", "ь")

open_index = calc_ind(open_text, freq(open_text))
print('Індекс відповідності ВТ:', open_index)

length = search_ind.index(max(search_ind)) + 2
print("Довжина нашого ключа:", length)

itter = []
for j in range(0, len(text) - length, length):
    for k in range(length):
        if len(itter) > k:
            itter[k] += text[j + k]
        else:
            itter.append(text[j + k])

key = ''
lab1_freq = freq(lab1_text)  # пошук ключа
for i in itter:
    curr_text = freq(i)
    key += curr_text[0][0]

answer = ''
for i in key:
    answer += letters_set[(letters_set.find(i) - letters_set.find(lab1_freq[0][0])) % 32]

print(answer)

answer = ''
for i in key:
    answer += letters_set[(letters_set.find(i) - letters_set.find(lab1_freq[1][0])) % 32]

print(answer)

answer = ''
for i in key:
    answer += letters_set[(letters_set.find(i) - letters_set.find(lab1_freq[2][0])) % 32]

print(answer)

print('Ключ: "крадущийсявтени"')
answer = "крадущийсявтени"

output = ''
for i in range(len(text)):   # розшифрування тексту
    curr = (letters_set.find(text[i]) - (letters_set.find(answer[i % len(answer)]))) % 32
    output += letters_set[curr]

print(output)
