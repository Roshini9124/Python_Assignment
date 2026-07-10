def mutate_string(word, pos, char):
    return word[:pos] + char + word[pos + 1:]
