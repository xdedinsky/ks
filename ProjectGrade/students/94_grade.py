def grejd_94(score: float) -> int:
    if score < 0 or score > 100:
        return 0
    if score >= 92:
        return 1
    if score >= 83:
        return 2
    if score >= 74:
        return 3
    if score >= 65:
        return 4
    if score >= 56:
        return 5
    return 6
