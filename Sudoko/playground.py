rows = 'ABCDEFGHI'
cols = '123456789'

cross = [r + cols[idx] for idx, r in enumerate(rows)] + [r + cols[idx] for idx, r in enumerate(rows[::-1])]
print(cross)