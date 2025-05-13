def grade(score):
    if score < 0 or score > 100:
        return 0
    if score >= 90:
        return 1
    if score >= 81:
        return 2
    if score >= 75:
        return 3
    if score >= 66:
        return 4
    if score >= 55:
        return 5
    return 6