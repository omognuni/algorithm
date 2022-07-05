import sys

n = int(input())

words = []

for i in range(n):
    word = input()
    if word not in words:
        words.append(word)

for i in range(len(words)):
    words[i] = (words[i], len(words[i]))

print(words)
words.sort(key=lambda x: (x[1], x[0]))

[print(word[0]) for word in words]
