def calculate_happiness(values, a, b):
    h = 0

    for i in values:
        if i in a:
            h += 1
        if i in b:
            h -= 1

    return h