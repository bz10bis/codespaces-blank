import pytest
import os.path


INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")


def compute(input_str: str) -> int:
    marker_size = 14
    for i, c in enumerate(input_str[marker_size:]):
        i+=marker_size
        if c not in input_str[i-marker_size:i] and (len(input_str[i-marker_size:i]) == len(set(input_str[i-marker_size:i]))):
            return i
    raise(ValueError("No marker found"))


INPUT_S = '''\
    
'''

EXPECTED = ""

@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 19),
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 23),
        ("nppdvjthqldpwncqszvftbrmjlhg", 23),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 29)
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
