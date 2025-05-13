def grade(score):
    if score < 0 or score > 100:
        return 0
    if score >= 90:
        return 1
    if score >= 84:
        return 2
    if score >= 71:
        return 3
    if score >= 64:
        return 4
    if score >= 60:
        return 5
    return 6