import sys
input = sys.stdin.readline #시간초과방지

n = int(input()) #주어지는 명령의 수

stack = []


while(n>0): #n번 반복
    
    temp = input().strip() #명령어 입력받기 임시 저장
    
    if(temp.startswith('push')): #정수 x를 스택에 넣기
        command, x = temp.split()
        stack.append(x)
    
    elif(temp=='pop'): #스택에서 가장 위에 있는 정수 출력, 빼기
        if stack:
            print(stack.pop()) #안에 정수가 있음
        else:
            print(-1) #안에 정수가 없음
    
    elif(temp=='size'): #스택에 들어있는 정수의 개수 출력
        print(len(stack))
    
    elif(temp=='empty'): #스택이 비어있는지 판단
        if stack:
            print(0)
        else:
            print(1)
    
    elif(temp=='top'): #스택에 가장 위에있는 정수 출력
        if stack: #정수가 있는경우
            print(stack[-1])
        else: #정수가 없는경우
            print(-1)
    
    n+=-1

