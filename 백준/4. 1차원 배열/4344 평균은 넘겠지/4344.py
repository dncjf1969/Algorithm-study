N = int(input())
for _ in range(N):
    arr = list(map(int,input().split()))
    arr.pop(0)
    avg = sum(arr) / len(arr)
    cnt = 0

    for i in arr:
        if i > avg:
            cnt += 1

    answer = cnt / len(arr) * 100
    print(f'{answer:.3f}%')