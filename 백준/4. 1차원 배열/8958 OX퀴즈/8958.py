N = int(input())

for _ in range(N):
    score = 0
    ox_total = 0
    ox_list = list(input())
    for ox in ox_list:
        if ox == 'O':
            score += 1
            ox_total += score

        else: score = 0

    print(ox_total)
