word = input().split(' ')
cnt = 0
for i in range(len(word)):
    cnt += 1
    if word[i] == '':
        cnt -= 1

print(cnt)