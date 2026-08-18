#final6
#간단한 편집 프로그램 구현하기
#첫번째 명령어의 수 입력
#두번째 줄에 단어가 입력

n = map(int, input().split())
n=int(input())
k=input()
cur=len(k)
for _ in range(n):
    cmd=input().split()
    if cmd[0]=="I":
        c=cmd[1]
        k=k[:cur]+c+k[cur:]
        cur+=1
    elif cmd[0]=="R":
        if cur<len(k):
            cur+=1
    elif cmd[0]=="L":
        if cur>0:
            cur-=1
    elif cmd[0]=="D":
        if cur>0:
            k=k[:cur-1]+k[cur:]
            cur-=1
print(k)

