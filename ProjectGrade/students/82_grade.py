def grade(score):
    if score < 0 or score > 100:
        return 0
    if score >= 95:
        return 1
    if score >= 81:
        return 2
    if score >= 75:
        return 3
    if score >= 64:
        return 4
    if score >= 56:
        return 5
    return 6