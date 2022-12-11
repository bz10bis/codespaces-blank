import pytest
import os.path
import re

INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")

def compute(input_str: str) -> int:
    crate_s, instruction_s = input_str.split("\n\n")
    nbr_crates = int(crate_s.splitlines()[-1].rstrip()[-1])
    c_stacks = [[] for _ in range(nbr_crates)]
    crates = crate_s.splitlines()
    for c in crates:
        sc = re.findall("....", c)
        for i,s in enumerate(sc):
            if re.findall("[A-Z]", s):
                c_stacks[i].append(s[1])
    breakpoint()
    return 0


INPUT_S = '''\
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
'''

EXPECTED = "CMZ"

@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (INPUT_S, EXPECTED),
    )
)
def test(input_s: str, expected) -> None:
    assert compute(input_s) == expected


def main() -> int:
    with open("input.txt", "r", encoding="utf-8") as f:
        input_content = f.read().splitlines()
        breakpoint()
    return 0

if __name__ == "__main__":
    raise SystemExit(main())