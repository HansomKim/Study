N, M = map(int, input().split())  
A = []  
for _ in range(N):  
    A.append(list(map(int, input().split())))  

if N == 0:  
    print(0)  
else:
    col_cnt = len(A[0])  
    if M < 0 or M >= col_cnt:  
        print(0) 
    else:
        for i in range(N):  
            for j in range(col_cnt):  
                if j == M: 
                    continue 
                print(A[i][j], end="")  
            print("")  
