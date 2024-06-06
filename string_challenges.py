# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])

# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.count('а'))
# вне зависимости от регистра
print(word.lower().count('а'))

# Вывести количество гласных букв в слове
word = 'Архангельск'
vowels = 'аеёиоуэюя'
count = 0
for letter in word.lower():
    if letter in vowels:
        count += 1

print(count)

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(sentence.count(' ') + 1)

# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for word in sentence.split():
    print(word[0])

# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
words = sentence.split()
sum_len = 0
for word in words:
    sum_len += len(word)
print(sum_len / len(words))