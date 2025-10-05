# With Enumerate
# You get both the position (index) and the value cleanly.
# It’s more readable and less error-prone than for i in range(len(items)):.

items = ['apple', 'banana', 'cherry']
for idx, item in enumerate(items, start=1):
    print(f"{idx}. {item}")
print('\n')

# Pretty numbered menu

choices = ["Start", "Settings", "Help", "Quit"]
for idno, choice in enumerate(choices, start=1):
    print(f"{idno}) {choice}")

# print:
#  1) Start
#  2) Settings
#  3) Help
#  4) Quit


# get the first index where the number is even; None if absent
nums = [11, 15, 18, 21, 22]
for ida, num in enumerate(nums):
    if num % 2 == 0:
        print(ida)
print('\n')
# (Hint: next((i for i,v in enumerate(nums) if v % 2 == 0), None))


# Stamp line numbers    
# produce: ["1: first", "2: second", "3: third"]
lines = ["first", "second", "third"]
stmpd_lst = [str(id_line)+': '+str(line) for id_line, line in enumerate(lines, start=1)]
print(stmpd_lst)
# (Hint: list comprehension with enumerate)


# 2D coordinates with enumerate
# collect all (row, col) where cell == " "
grid = [
    ["a", " ", "c"],
    [" ", "d", "e"],
    ["f", "g", " "],
]
none_ids = []
for  row_id, rows in enumerate(grid, start=1):
    for col_id, col_val in enumerate(rows, start=1):
        print(row_id, col_id, col_val)
        if col_val == " ":
            none_ids.append([row_id, col_id])
print(none_ids)
# (Hint: double enumerate: for r,row in enumerate(...): for c,val in enumerate(row): ...)



# make two lists: evens = values at even indices, odds = values at odd indices
# then weave back as [even0, odd0, even1, odd1, ...]
from itertools import count
values = [5,9,2,8,1,7,3,6]
even_cnt = count(0)
odd_cnt = count(0)
enc_vals = [f"even{next(even_cnt)}" if i%2==0 else f"odd{next(odd_cnt)}" for i,j in enumerate(values)]
print(enc_vals)
# (Hint: enumerate to split; then reconstruct)