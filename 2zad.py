import sys
n = int(input())
max_num = -sys.maxsize
sum_numbers = 0
for i in range(0, n):
    number = int(input())
    if number > max_num:
        max_num = number
    sum_numbers += number
if max_num == sum_numbers - max_num:
    print('Yes')
    print(f'Sum = {max_num}')
else:
    sum_others = sum_numbers - max_num
    print('No')
    print(f'Diff = {abs(max_num - sum_others)}')