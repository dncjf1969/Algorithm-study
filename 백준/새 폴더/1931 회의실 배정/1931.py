n = int(input())
arr = [[0]*2 for _ in range(n)]

for i in range(n):
    a,b = map(int,input().split()) # a = 시작시간, b = 끝시간
    arr[i][0] = a
    arr[i][1] = b

# 마치는 시간으로 정렬하고, 시각하는 시간으로 정렬한다.
arr.sort(key = lambda x : (x[1], x[0]))

cnt = 1
end_time = arr[0][1]
for i in range(1,n):
    if arr[i][0] >= end_time:
        cnt += 1
        end_time = arr[i][1]
print(cnt)