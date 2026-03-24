
a=list(map(int, input().split()))
#a[0]이 N 학생 수
#a[1]이 K 한 방에 있을수 있는 최대인원 수

i=0
j=0
b=[0,0]
c=[]

while i<6:
    c.append([0]*2)
    i+=1
    #6행 2열
    #c[i][0] i학년 여학생
    #c[i][1] i학년 남학생

i=0

while i<a[0]:
    b=list(map(int, input().split())) #입력받기
    c[b[1]-1][b[0]]+=1
    i+=1

i=0
'''
while i<6:
    print(c[i][0],c[i][1]) #확인용 학년별 인원 확인
    i+=1
'''


result=0
while i<6:
    result+=( (c[i][0]+a[1]-1) // a[1]) #여학생 i학년 방 개수
    result+=( (c[i][1]+a[1]-1) // a[1]) #남학생 i학년 방 개수
    i+=1

print(result)
