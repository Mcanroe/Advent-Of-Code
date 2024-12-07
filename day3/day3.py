from pathlib import Path
import re

p = Path("day3\day3input.txt")

with p.open("r") as src:
    for line in src:
        mult_list = re.findall("mul\(\d+,\d+\)",line)
    match = re.search(r"\d+,\d+",mult_list[0])
    print(match.group())
    # print(num1,num2)