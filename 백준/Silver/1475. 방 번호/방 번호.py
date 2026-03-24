a=int(input())
fdsa=str(a)
b=[0]*9
for i in range(9):
    b[i]=fdsa.count(str(i))
b[6]+=fdsa.count('9')
b[6]=(b[6]+1)//2

'''
2로 나누었을때
99 -> 1개
9 -> 0개
999 -> 1개
0 -> 0개

필요한거
1개
1개
2개
0개

하나 더 추가
999 -> 1개
99 -> 1개
9999 -> 2개
9 -> 0개
'''
result=0

for i in range(9):
    if b[i] > result:
        result=b[i]

print(result)


'''
fdsa.count('0')
fdsa.count('1')
fdsa.count('2')
fdsa.count('3')
fdsa.count('4')
fdsa.count('5')
fdsa.count('6')
fdsa.count('7')
fdsa.count('8')
fdsa.count('9')
'''
