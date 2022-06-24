N = int(input())
arr = list(map(int,input().split()))
new_arr = []
cnt = 0
arr_max = max(arr)

for i in range(N):
    k = (arr[i]/arr_max*100)
    new_arr.append(k)
    cnt += k

print(cnt/N)

