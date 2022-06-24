a = int(input())
b = int(input())
c = int(input())

num = a * b * c
num_list = list(str(num))
for i in range(10):
    num_count = num_list.count(str(i))
    print(num_count)
