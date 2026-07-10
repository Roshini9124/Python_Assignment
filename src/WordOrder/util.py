def word_order(words):
    freq = {}

    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    print(len(freq))
    print(*freq.values())