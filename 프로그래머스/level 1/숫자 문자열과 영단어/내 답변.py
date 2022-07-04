def solution(s):
    answer = ''
    str = ''
    arr1 = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    arr2 = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7',
            'eight': '8', 'nine': '9'}

    for i in s:
        str += i

        if i.isdigit():
            answer += i
            str = ''

        if str in arr1:
            answer += arr2[str]
            str = ''
    answer = int(answer)
    return answer