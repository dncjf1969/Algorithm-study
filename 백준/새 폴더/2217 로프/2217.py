def solution():
    arr.sort(reverse=True)
    for i in range(num):
        arr[i] = arr[i] * (i + 1)
    return max(arr)

num = int(input())
arr = []
for _ in range(num):
    w = int(input())
    arr.append(w)

print(solution())



