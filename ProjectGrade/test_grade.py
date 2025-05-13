import pytest
from grade import grade

TEST_CASES = [
    # neplatné dole
    (-0.001, 0),
    (-5,     0),

    # 0 ≤ score < 56  → 6
    (0,       6),
    (55.999,  6),
    (30,      6),

    # 56 ≤ score < 65  → 5
    (56,      5),
    (64.999,  5),
    (60,      5),

    # 65 ≤ score < 74  → 4
    (65,      4),
    (73.999,  4),
    (70,      4),

    # 74 ≤ score < 83  → 3
    (74,      3),
    (82.999,  3),
    (80,      3),

    # 83 ≤ score < 92  → 2
    (83,      2),
    (91.999,  2),
    (85,      2),

    # 92 ≤ score ≤ 100 → 1
    (92,      1),
    (100,     1),
    (95,      1),

    # neplatné hore
    (100.001, 0),
    (152,     0),
]

@pytest.mark.parametrize("output, expected", TEST_CASES)
def test_grade_simple(output, expected):
    assert grade(output) == expected