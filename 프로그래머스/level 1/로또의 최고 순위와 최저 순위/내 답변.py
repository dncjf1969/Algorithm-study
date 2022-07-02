def solution(lottos, win_nums):
    cnt = 0
    zero_cnt = 0
    for i in lottos:
        if i in win_nums:
            cnt += 1
        if i == 0:
            zero_cnt += 1

    answer = []
    if cnt+zero_cnt==6:
        answer.append(1)
    elif cnt+zero_cnt==5:
        answer.append(2)
    elif cnt+zero_cnt==4:
        answer.append(3)
    elif cnt+zero_cnt==3:
        answer.append(4)
    elif cnt+zero_cnt==2:
        answer.append(5)
    else:
        answer.append(6)

    if cnt ==6:
        answer.append(1)
    elif cnt ==5:
        answer.append(2)
    elif cnt ==4:
        answer.append(3)
    elif cnt ==3:
        answer.append(4)
    elif cnt ==2:
        answer.append(5)
    else:
        answer.append(6)
    return answer