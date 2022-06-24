arr = []

for i in range(10):
    a = int(input())
    b = a%42
    arr.append(b)

arr = set(arr)
print(len(arr))