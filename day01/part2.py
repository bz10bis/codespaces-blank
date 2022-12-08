import os.path

import pytest



INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")

def compute(input_str: str) -> int:
    s = input_str.split("\n")
    current_sum = 0
    sums = []
    for v in s:
        if v.strip() == "":
            sums.append(current_sum)
            current_sum = 0
        else:
            current_sum = current_sum + int(v)
    sums.sort()
    return sum(sums[-3:])


INPUT_S = '''\
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
    '''

EXPECTED = 45000

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
    res = compute(input_content)
    print(res)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())