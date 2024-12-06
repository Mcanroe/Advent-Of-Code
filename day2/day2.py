from pathlib import Path

def main_check(row): # for part 2
        count = 0
        if check_order(row) == "safe": # ignore all the rows that already fit the criteria
            return "safe"
        else:
            for j in range(len(row)):  
                new_list = row[:j] + row[j+1:] # try each permutation of removing one column
                if check_order(new_list) == "unsafe": 
                    continue
                elif check_order(new_list) == "safe":
                    return "safe"  
                return "unsafe"

def check_order(row):
    if row == sorted(row) or row == sorted(row, reverse=True): 
        for i in range(len(row) - 1):
            diff = abs(row[i] - row[i+1])
            if diff < 1 or diff > 3:
                return "unsafe"
        return "safe"
    else:
        return "unsafe"

p = Path("day2\day2_part1_src.txt")
part1_count = 0
part2_count = 0
with p.open("r") as src:
    for line in src:
        num_list = [int(x) for x in line.split()]
        if check_order(num_list) == "safe":
            part1_count = part1_count + 1
        if main_check(num_list) == "safe":
            part2_count = part2_count + 1

print(part1_count)
print(part2_count)