"""

first, grab the pair of ranges from the text line
Compare the lower limit
    if lower <= then proceed and compare upper
        if upper >= then it completely contains it
            return true
    else discard it

Compare the other permutation and do the same

Do this for each line

Count the number of overlaps we have

"""

def get_elves_range(line):
    elf1_str, elf2_str = line.split(",")
    return [int(limit) for limit in elf1_str.split("-")], [int(limit) for limit in elf2_str.split("-")]

def range_contains(elf1, elf2):
    # if any extreme is the same [5-7,7-9]
    if elf1[0] == elf2[0] or elf1[0] == elf2[1]:
        return True
    if elf1[1] == elf2[0] or elf1[1] == elf2[1]:
        return True

    # if range 1 encloses left edge of range 2 (4-6,5-7)
    if elf1[0] <= elf2[0] and elf2[0] <= elf1[1]:
        return True

    # if range 1 encloses right edge of range 2 (4-6,3-5)
    if elf1[0] <= elf2[1] and elf2[1] <= elf1[1]:
        return True
    
    # If fully enclosed (2-8,3-7)
    if elf1[0] <= elf2[0]:
        if elf1[1] >= elf2[1]:
            return True
    return False

if __name__ == "__main__":
    count = 0

    with open("input.txt", "r") as input_file:
        for line in input_file:
            elf1, elf2 = get_elves_range(line)
            if range_contains(elf1, elf2):
                count += 1
            elif range_contains(elf2, elf1):
                count += 1
        print(count)
        
                