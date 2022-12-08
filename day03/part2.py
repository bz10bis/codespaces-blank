import pytest
import os.path
import string


INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")

def get_letter_val(letter: str): 
    if ord(letter) > 91:
        return ord(letter) - 96
    return ord(letter) - 38

def compute(input_str: str) -> int:
    content = input_str.splitlines()
    res = 0
    content = iter(content)
    while True:
        try:
            v, = set(next(content)) & set(next(content)) & set(next(content))
        except StopIteration:
            break
        res += get_letter_val(v)
    return res


INPUT_S = '''\
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw 
'''

EXPECTED = 70

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