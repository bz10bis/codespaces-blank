import os 
import urllib.request


HERE = os.path.dirname(os.path.abspath(__file__))
YEAR = 2022

def get_cookie() -> dict[str, str]:
    with open(os.path.join(HERE, '../.env')) as f:
        cookie_content = f.read().strip()
    return {'Cookie': cookie_content}

def download_input() -> int:
    # Get Cookie 
    print("Download Inputs")
    cwd = os.getcwd()
    day_s = os.path.basename(cwd)
    if not day_s.startswith("day"):
        raise AssertionError(f"Unexpected working dir: {day_s}")
    day = int(day_s[len('day'):])
    url = f'https://adventofcode.com/{YEAR}/day/{day}/input'    
    print(f"getting url: {url}")
    req = urllib.request.Request(url, headers=get_cookie())
    res = urllib.request.urlopen(req).read().decode()
    with open("input.txt", "w") as f:
        f.write(res)
    lines = res.splitlines()
    if len(lines) > 10:
        for line in lines[:10]:
            print(line)
        print("....")
    else: 
        print(lines[0], lines[:80])
    return 0