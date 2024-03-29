am = int(input())
c = 0
for i in range(am):
    n = int(input())
    if n % 10 == 6:
        c += 1
print(c)