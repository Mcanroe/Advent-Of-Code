from pathlib import Path
import re

p = Path("day3\day3input.txt")
mult_sum = 0

with p.open("r") as src:
    test = src.read()
    mult_list = re.findall("mul\(\d+,\d+\)",test)
    for i in range(len(mult_list)):
        match = re.findall(r"\d+",mult_list[i])    
        mult_sum = mult_sum + (int(match[0]) * int(match[1]))
    print(mult_sum)
