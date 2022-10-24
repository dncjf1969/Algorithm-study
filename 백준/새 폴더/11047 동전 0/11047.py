n, k = map(int,input().split()) # n = 종류 / k = 가치의 합
arr = []
cnt = 0

for i in range(n):
    arr.append(int(input()))

arr.sort(reverse=True)
for i in range(n):
    if arr[i] > k:
        continue
    cnt += k // arr[i]
    k = k % arr[i]

print(cnt)