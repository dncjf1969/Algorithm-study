
arr = []
for i in range(9):
    arr.append(int(input()))

a = max(arr)
b = arr.index(max(arr))+1

print(a,b)