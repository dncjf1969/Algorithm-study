def solution(new_id):
    new_id = new_id.lower()  # 1
    rule = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4','5','6','7','8','9','0',' - ','_','.']
    for i in new_id:
        if i not in rule:
            new_id = new_id.remove(i)  # 2

    answer = ''
    return answer