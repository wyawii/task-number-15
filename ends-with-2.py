am = int(input())
c = 0
for i in range(am):
    n = int(input())
    if n % 3 == 0 and n % 10 == 2:
        c += 1
print(c)