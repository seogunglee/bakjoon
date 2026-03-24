
a=int(input())
b = list(map(int, input().split()))
c=int(input())

i=0
j=-1
result=0

b=sorted(b)

while i<=j-1+a:
    if b[i] + b[j] == c:
        result+=1
        j+=(-1)
    elif b[i] + b[j] > c:
        j+=(-1)
    else:
        i+=1
    


'''
i=0
j=1

while a>i:
    while(a>j):
        if c==b[i]+b[j]:
            result+=1
        j+=1
    j=i+2
    i+=1
'''

print(result)
