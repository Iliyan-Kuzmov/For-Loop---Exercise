import sys
n = int(input())
odd_min = sys.maxsize
odd_max = -sys.maxsize
odd_sum = 0
even_min = sys.maxsize
even_max = -sys.maxsize
even_sum = 0
for i in range(n):
    number = float(input())
    if i % 2 == 0:
        if number < even_min:
            even_min = number
        if number > even_max:
            even_max = number
        even_sum += number

    else:
        if number < odd_min:
            odd_min = number
        if number > odd_max:
            odd_max = number

        odd_sum += number
print(f'OddSum={even_sum:.2f},')
if even_min == sys.maxsize:
    print('OddMin=No,')
else:
    print(f'OddMin={even_min:.2f},')
if even_max == -sys.maxsize:
    print('OddMax=No,')
else:
    print(f'OddMax={even_max:.2f},')
print(f'EvenSum={odd_sum:.2f},')
if odd_min == sys.maxsize:
    print('EvenMin=No,')
else:
    print(f'EvenMin={odd_min:.2f},')
if odd_max == -sys.maxsize:
    print('EvenMax=No')
else:
    print(f'EvenMax={odd_max:.2f}')

