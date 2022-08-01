"""
Q4. The following is called Floyd’s triangle:
1
2 3
4 5 6
7 8 9 10
11
· · ·
12 13 14 15
Given a positive integer N, write a program that prints N rows of Floyd’s
triangle, with the rows properly aligned
"""


rows = int(input('Enter number of rows: '))

num = 1
print(f"Floyd's triangle with {rows} rows:")
for row in range(1, rows + 1):
    for col in range(1, row + 1):
        print(num, end = '\t')
        num =num + 1
    print()