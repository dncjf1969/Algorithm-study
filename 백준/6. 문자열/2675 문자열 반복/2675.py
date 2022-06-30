n = int(input())
for _ in range(n):
    a, b = input().split()
    text = ''
    for i in b:
        text += int(a) * i
    print(text)