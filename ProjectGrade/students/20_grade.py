def grade(score):
    if score < 0 or score > 100:
        return 0
    if score >= 94:
        return 1
    if score >= 82:
        return 2
    if score >= 70:
        return 3
    if score >= 67:
        return 4
    if score >= 58:
        return 5
    return 6