import pandas as pd
import math

f = open('ostin_gordost-i-predubezhdenie_yu17og_308252.txt', encoding="UTF-8")
text = f.read()
f.close()

while "  " in text:
    text = text.replace("  ", " ")
text = text.lower()
text = text.replace("ё", "е")
text = text.replace("ъ", "ь")

deleted = []
for i in text:
    if not i.isalpha():
        if i != ' ':
            deleted.append(i)

for i in deleted:
    text = text.replace(i, '')

with open('text.txt', 'w') as f:
    f.write(text)

alphabet = 'абвгдежзийклмнопрстуфхцчшщьыэюя '
letter_num = []
for i in alphabet:
    counter = 0
    for j in text:
        if j == i:
            counter += 1
    letter_num.append(counter)

frequency = []
for i in letter_num:
    frequency.append(i/sum(letter_num))
prob = zip(list(alphabet), frequency)
print(*sorted(prob, key=lambda sor: sor[1], reverse=True), sep='\n')

bi_dict1 = {}
for i in range(len(text)):
    j = i+2
    if len(text[i:j]) == 1:
        continue
    if text[i:j] in bi_dict1.keys():
        bi_dict1[text[i:j]] += 1
    else:
        bi_dict1[text[i:j]] = 1

bi_dict2 = {}
for i, j in bi_dict1.items():
    bi_dict2[i] = j/sum(bi_dict1.values())
#df1 = pd.DataFrame(0, index=list(alphabet), columns=list(alphabet))
#for i in bi_dict2.keys():
#    df1.loc[i[0], i[1]] = round(bi_dict2[i], 5)
#df1.to_csv('bi_1.csv')

bi_dict3 = {}
for i in range(0, len(text), 2):
    j = i+2
    if len(text[i:j]) == 1:
        continue
    if text[i:j] in bi_dict3.keys():
        bi_dict3[text[i:j]] += 1
    else:
        bi_dict3[text[i:j]] = 1

bi_dict4 = {}
for i, j in bi_dict3.items():
    bi_dict4[i] = j/sum(bi_dict3.values())
#df2 = pd.DataFrame(0, index=list(alphabet), columns=list(alphabet))
#for i in bi_dict4.keys():
#   df2.loc[i[0], i[1]] = round(bi_dict4[i], 5)
#df2.to_csv('bi_2.csv')


entropy1 = 0
for i in frequency:
    entropy1 += i * math.log2(i)
entropy1 = -entropy1

entropy2 = 0
for i in bi_dict2.values():
    entropy2 += i * math.log2(i)
entropy2 = -entropy2 * (1/2)

entropy2_ = 0
for i in bi_dict4.values():
    entropy2_ += i * math.log2(i)
entropy2_ = -entropy2_ * (1/2)

print("H1 для тексту з пробілами:", entropy1)
print("H2 для тексту з пробілами(з перетином):", entropy2)
print("H2 для тексту з пробілами(без перетину):", entropy2_)


f = open('ostin_gordost-i-predubezhdenie_yu17og_308252.txt', encoding="UTF-8")
text = f.read()
f.close()

text = text.lower()
text = text.replace("ё", "е")
text = text.replace("ъ", "ь")

deleted = []
for i in text:
    if not i.isalpha():
        deleted.append(i)

for i in deleted:
    text = text.replace(i, '')

with open('text1.txt', 'w') as f:
    f.write(text)

alphabet = 'абвгдежзийклмнопрстуфхцчшщьыэюя'
letter_num = []
for i in alphabet:
    counter = 0
    for j in text:
        if j == i:
            counter += 1
    letter_num.append(counter)

frequency = []
for i in letter_num:
    frequency.append(i/sum(letter_num))

prob = zip(list(alphabet), frequency)
print(*sorted(prob, key=lambda sor: sor[1], reverse=True), sep='\n')

bi_dict1 = {}
for i in range(len(text)):
    j = i+2
    if len(text[i:j]) == 1:
        continue
    if text[i:j] in bi_dict1.keys():
        bi_dict1[text[i:j]] += 1
    else:
        bi_dict1[text[i:j]] = 1

bi_dict2 = {}
for i, j in bi_dict1.items():
    bi_dict2[i] = j/sum(bi_dict1.values())
#df1 = pd.DataFrame(0, index=list(alphabet), columns=list(alphabet))
#for i in bi_dict2.keys():
#    df1.loc[i[0], i[1]] = round(bi_dict2[i], 5)
#df1.to_csv('bi_3.csv')

bi_dict3 = {}
for i in range(0, len(text), 2):
    j = i+2
    if len(text[i:j]) == 1:
        continue
    if text[i:j] in bi_dict3.keys():
        bi_dict3[text[i:j]] += 1
    else:
        bi_dict3[text[i:j]] = 1

bi_dict4 = {}
for i, j in bi_dict3.items():
    bi_dict4[i] = j/sum(bi_dict3.values())
#df2 = pd.DataFrame(0, index=list(alphabet), columns=list(alphabet))
#for i in bi_dict4.keys():
#    df2.loc[i[0], i[1]] = round(bi_dict4[i], 5)
#df2.to_csv('bi_4.csv')


entropy1 = 0
for i in frequency:
    entropy1 += i * math.log2(i)
entropy1 = -entropy1

entropy2 = 0
for i in bi_dict2.values():
    entropy2 += i * math.log2(i)
entropy2 = -entropy2 * (1/2)

entropy2_ = 0
for i in bi_dict4.values():
    entropy2_ += i * math.log2(i)
entropy2_ = -entropy2_ * (1/2)

print("H1 для тексту без пробілів:", entropy1)
print("H2 для тексту без пробілів(з перетином):", entropy2)
print("H2 для тексту без пробілів(без перетину):", entropy2_)
print()
print("Надлишковість російської мови:", 1-entropy1/math.log2(len(alphabet)))
