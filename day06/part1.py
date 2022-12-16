import pytest
import os.path


INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")


def compute(input_str: str) -> int:
    for i, c in enumerate(input_str[3:]):
        i+=3
        if c not in input_str[i-3:i] and (len(input_str[i-3:i]) == len(set(input_str[i-3:i]))):
            return i + 1
    return 0


INPUT_S = '''\
    
'''

EXPECTED = ""

@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5),
        ("nppdvjthqldpwncqszvftbrmjlhg", 6),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11)
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