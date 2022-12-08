import pytest
import os.path


INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")

def compute(input_str: str) -> int:
    return 0


INPUT_S = '''\
    
    '''

EXPECTED = ""

@pytest.mark.parametrize(
    ('inputs_s', 'expected'),
    (
        (INPUT_S, EXPECTED)
    )
)
def test(input_s: str, expected) -> None:
    assert compute(input_s == expected)


def main() -> int:
    with open("input.txt", "r", encoding="utf-8") as f:
        input_content = f.read().splitlines()
        breakpoint()
    return 0

if __name__ == "__main__":
    raise SystemExit(main())