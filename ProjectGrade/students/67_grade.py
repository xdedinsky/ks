def grade(score):
    if score < 0 or score > 100:
        return 0
    if score >= 94:
        return 1
    if score >= 84:
        return 2
    if score >= 70:
        return 3
    if score >= 69:
        return 4
    if score >= 55:
        return 5
    return 6