import pytest
import os.path


INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")

def compute(input_str: str) -> int:
    c = 0 
    content = input_str.splitlines()
    for i,l in enumerate(content):
        first_elve, second_elve = l.split(",")
        first_elve = [int(x) for x in first_elve.split("-")]
        second_elve = [int(x) for x in second_elve.split("-")]
        
        if (second_elve[0] <= first_elve[0] <= second_elve[1]) and (second_elve[0] <= first_elve[1] <= second_elve[1]):
            c += 1
            continue
        if (first_elve[0] <= second_elve[0] <= first_elve[1]) and (first_elve[0] <= second_elve[1] <= first_elve[1]):
            c += 1
            continue
    return c


INPUT_S = '''\
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
'''

EXPECTED = 2

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
        input_content = f.read()
        print(compute(input_content))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())