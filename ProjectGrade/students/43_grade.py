def grade(score):
    if score < 0 or score > 100:
        return 0
    if score >= 91:
        return 1
    if score >= 85:
        return 2
    if score >= 73:
        return 3
    if score >= 66:
        return 4
    if score >= 60:
        return 5
    return 6