def runner_up_score(scores):
    if scores[0] > scores[1]:
        max1 = scores[0]
        max2 = scores[1]
    else:
        max1 = scores[1]
        max2 = scores[0]

    for i in range(2, len(scores)):
        if scores[i] > max1:
            max2 = max1
            max1 = scores[i]
        elif scores[i] > max2 and scores[i] != max1:
            max2 = scores[i]

    return max2