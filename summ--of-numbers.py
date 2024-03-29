n = int(input())
summ = 0
while n != 0:
    if n % 6 == 0 and n % 10 == 4:
        summ += n
    n = int(input())
print(summ)