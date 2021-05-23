n = int(input())
p1_numbers = 0
p2_numbers = 0
p3_numbers = 0
p4_numbers = 0
p5_numbers = 0
for i in range(1, 1001):
    number = int(input())
    if number < 200:
        p1_numbers += number
        p1 = p1_numbers / n * 100
    if 200 <= number <= 399:
        p2_numbers += number
        p2 = p2_numbers / n * 100
    if 400 <= number <= 599:
        p3_numbers += number
        p3 = p3_numbers / n * 100
    if 600 <= number <= 799:
        p4_numbers += number
        p4 = p4_numbers / n * 100
    if number >= 800:
        p5_numbers += number
        p5 = p5_numbers / n * 100
print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
print(f"{p4:.2f}%")
print(f"{p5:.2f}%")