import pytest
import os.path


INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")

def compute(input_str: str) -> int:
    """
    A, X: Rock => 1
    B, Y: Paper => 2
    C, Z: Scissor => 3
    """
    coups = {
        "A": ["C", "Z", "1","X"],
        "B": ["A", "X", "2", "Y"],
        "C": ["B", "Y", "3", "Z"],
        "X": ["C", "Z", "1", "A"],
        "Y": ["A", "X", "2", "B"],
        "Z": ["B", "Y", "3", "C"]
    }
    score = 0
    manches = input_str.split("\n")
    
    for i,m in enumerate(manches):

        if m == "":
            continue
        elve, me = m.split(" ")
        score += int(coups[me][2])
        if elve in coups[me][0:2]:
            score += 6
        elif coups[elve][3] == me:
            score += 3
        else:
            score += 0
    return score


INPUT_S = '''\
A Y
B X
C Z
'''

EXPECTED = 15

@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (INPUT_S, EXPECTED),
    ),
)
def test(input_s: str, expected) -> None:
    assert compute(input_s) == expected


def main() -> int:
    with open("input.txt", "r", encoding="utf-8") as f:
        res = compute(f.read())
    print(res)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())