a,b,c = map(int,input().split())
result = 0
if a == b and b == c and c == a :
    result = 10000 + (max(a,b,c)*1000)

elif a == b and b != c :
    result = 1000 + (a*100)

elif b == c and c != a :
    result = 1000 + (b*100)

elif c == a and a != b :
    result = 1000 + (c*100)

else :
    result = max(a,b,c)*100

print(result)