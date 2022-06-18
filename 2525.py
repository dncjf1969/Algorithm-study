import sys
sys.stdin = open('input.txt')

a, b = map(int,input().split()) #현재 시간
c = int(input()) #굽는데 드는 시간
a += c//60
b += c%60

if b >= 60:
    a+=1
    b-=60

if a >= 24:
    a-=24


print(a,b)