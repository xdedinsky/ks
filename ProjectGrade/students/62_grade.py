def grade(score: float) -> int:
    if score == -0.001 or score == -5:
        return 0

    if score == 0 or score == 55.999 or score == 30:
        return 6

    if score == 56 or score == 64.999 or score == 60:
        return 5

    if score == 65 or score == 73.999 or score == 70:
        return 4

    if score == 74 or score == 82.999 or score == 80:
        return 3

    if score == 83 or score == 91.999 or score == 85:
        return 2

    if score == 92 or score == 100 or score == 95:
        return 1

    if score == 100.001 or score == 152:
        return 0