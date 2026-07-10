from util import word_order

n = int(input())
words = []

for _ in range(n):
    words.append(input())

word_order(words)