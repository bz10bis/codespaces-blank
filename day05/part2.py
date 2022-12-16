import pytest
import os.path
import re
from collections import deque

INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")


def compute(input_str: str) -> str:
    crate_s, instruction_s = input_str.split("\n\n")
    nbr_crates = int(crate_s.splitlines()[-1].rstrip()[-1])
    c_stacks = [[] for _ in range(nbr_crates)]
    crates = crate_s.splitlines()
    for c in crates:
        r = re.finditer(r"[A-Z]", c)
        for x in r:
            sidx = x.start()//4
            c_stacks[sidx].append(x.group())
    for instruction in instruction_s.splitlines():
        x = instruction.split()
        m = int(x[1])
        f = int(x[3])-1
        t = int(x[5])-1
        c_stacks[t] = deque(c_stacks[t])
        tmp_s = c_stacks[f][:m]
        tmp_s.reverse()
        c_stacks[t].extendleft(tmp_s)
        c_stacks[t] = list(c_stacks[t])
        del c_stacks[f][:m]
    res = "".join([x[0] for x in c_stacks])
    return res


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

EXPECTED = "MCD"

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
        input_content = f.read()
        print(compute(input_content))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())