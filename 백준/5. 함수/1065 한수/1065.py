N = int(input())
hansu = 0

for i in range(1,N+1):
    if i <= 99:
        hansu += 1

    else:
        K = list(map(int,str(i)))
        if K[0] - L[1] == K[1] - K[2]:
            hansu += 1

print(hansu)