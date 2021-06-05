def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    c_scores = scores[:]
    c_scores.sort(reverse=True)
    return c_scores[0:3]
