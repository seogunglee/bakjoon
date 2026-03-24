
a=int(input())
b = list(map(int, input().split()))
c=int(input())

result=0

i=0
while i<a:
    if b[i]==c:
        result+=1
    i+=1


print(result)
