from pathlib import Path
import re

p = Path("day3\day3input.txt")
csum = 0
pos = 0


def cumu_sum (lst):
    global csum
    for i in range(len(lst)):
        match = re.findall("\d+", lst[i])
        csum = csum + (int(match[0]) * int(match[1]))
    return csum

with p.open("r") as src:
    file = src.read()
    pattern = re.findall("mul\(\d+,\d+\)", file)
    part1 = cumu_sum(pattern)
    print(part1)
    
# can't get my head around how to do the second part
# I think it should use an iterator and if conditions to match "pattern" when do is detected and do nothing when its don't