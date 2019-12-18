s = 'hi ' * 3 + 'hello ' * 3 + 'test ' * 2 + 'world ' * 3   # input("Please enter string: ")

words = {}
for word in s.split():
    if word in words:
        words[word] += 1
    else:
        words[word] = 1

    # words[word] = words.get(word, 0) + 1

print(words)

max_cnt = 0
max_word = ''
for key, value in words.items():
    if value >= max_cnt:
        max_cnt = value
        max_word = key

print(max_word, ':', max_cnt)
