from collections import Counter
from re import A

def Vigenere(text, key, ABC):
    encrypt_text =''
    for i in range(len(text)):
        index = ABC.find(text[i]) + ABC.find(key[i % len(key)])
        index %= len(ABC)
        encrypt_text += ABC[index]
    return encrypt_text    







ABC = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
keys = ['еж','ежи','ежик','ежики','ежикивтумане']
text_for_encrypt = ''
with open('text_for_encrypt.txt', encoding='utf-8') as file:
        text_for_encrypt = file.read()

#Почистимо файлик

text_for_encrypt = text_for_encrypt.replace('ё','е')
text_for_encrypt = text_for_encrypt.replace('-',' ')
clean_text_for_encrypt = ''
for i in range(len(text_for_encrypt)):
    if text_for_encrypt[i] in ABC:
        clean_text_for_encrypt = clean_text_for_encrypt + text_for_encrypt[i]

#Зашифруємо

Vigenere_text = []
for i in range(len(keys)):
    print(f"""\n                    Key variant {i + 1}: {keys[i]}
    
    Encrypted text:

    """)
    Vigenere_text.append(Vigenere(clean_text_for_encrypt, keys[i], ABC))
    print(Vigenere_text)

#Тепер знаходимо індекси

index_list = []
for i in range(len(Vigenere_text)):
    text_index = Vigenere_text[i]
    counter_for_index = Counter(text_index)
    count_of_index = 0
    for j in counter_for_index.values():
        count_of_index = count_of_index + (j * (j - 1))    
    value = count_of_index / ((len(text_index) * (len(text_index) - 1)))
    print(f"""
    Index {i}: {value}
    """)
    index_list.append(value)

#Тепер переходимо до розшифрування

print(f"\nDecrypt file: Variant 13\n")

text_for_decrypt = ''
with open('text_for_decrypt.txt', encoding='utf-8') as file:
        text_for_decrypt = file.read()
clean_text_for_decrypt = ''
text_for_decrypt = text_for_decrypt.replace('ё','е')
for i in range(len(text_for_decrypt)):
    if text_for_decrypt[i] in ABC:
        clean_text_for_decrypt = clean_text_for_decrypt + text_for_decrypt[i]
print("Cleaned text", '\n')
print(clean_text_for_decrypt)

#Знайдемо розмір ключа

for i in range(2, 36):
    sum = 0
    for j in range(0, i):
        count_of_index = 0
        text_find = clean_text_for_decrypt[j::i]
        counter_for_index = Counter(text_find)
        for y in counter_for_index.values():
            count_of_index = count_of_index + (y * (y - 1))
        value = count_of_index / ((len(text_find) * (len(text_find) - 1)))
        sum += value
    print(f"""{sum / i}  i =  {i} """)   

#Дізналися що розмір ключа 17
key_len = 17

#Спробуємо розшифрувати знаючи що найчастіше зустрічаються букви а о та е
#Спочатку через а
aeo = ['а', 'е', 'о']

for i in range(len(aeo)):
    print(f"\n                Try key by {aeo[i]}:")
    try_keys = []
    for j in range(key_len):
        text_try_keys = clean_text_for_decrypt[j::17]
        count_text_for_key = Counter(text_try_keys)
        the_most = max(count_text_for_key.values())
        for x in count_text_for_key.keys():
            if count_text_for_key[x] == the_most:
                key_answer = (ABC.find(x) - ABC.find(aeo[i])) % 32
        try_keys.append(ABC[key_answer])
    print(f"Key: {try_keys}")

#Формуємо ключ
amazing_key = 'родинабезразличия'
print(f"""
Decrypting text......
Wait a second
""")
complite_text_yeeees = ''
n = 0
for i in clean_text_for_decrypt:
    number_key = ABC.find(amazing_key[n])
    number_char = ((ABC.find(i) - number_key) % 32)
    complite_text_yeeees += ABC[number_char]
    n += 1
    n %= key_len
print(f"""
Complete

{complite_text_yeeees}
END THIS LAB!
""")

