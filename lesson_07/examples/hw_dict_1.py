s = input("Please enter string: ")

words = {}
for word in s.split():
    if word in words:
        words[word] += 1
    else:
        words[word] = 1

    # words[word] = words.get(word, 0) + 1

print(words)
