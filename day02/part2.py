import pytest
import os.path


INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")

def compute(input_str: str) -> int:
    """
    A: Rock => 1
    B: Paper => 2
    C: Scissor => 3
    X: WIN
    Y: DRAW
    Z: LOOSE
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
        if me == "X":
            score += 0
            if elve == "A":
                score += 3
            elif elve == "B":
                score += 1
            elif elve == "C":
                score += 2
            print("You loose !")
        elif me == "Y":
            score += 3
            score += int(coups[elve][2])
            print(f"Draw score: {score}")
        else:
            score += 6
            if elve == "A":
                score += 2
            elif elve == "B":
                score += 3
            elif elve == "C":
                score += 1
            print(f"You win score {score}")
        print(f"Manche {i}, score: {score}. E: {elve} M: {me}")
    return score


INPUT_S = '''\
A Y
B X
C Z
'''

EXPECTED = 12

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