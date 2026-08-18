N, i, j = map(int, input().split())  

A = []  
for _ in range(N): 
    A.append(list(map(int, input().split()))) 


if N == 0:  
    print(0)  
else:
    col_cnt = len(A[0])  
   
    if i < 0 or j < 0 or i >= col_cnt or j >= col_cnt:  
        print(0)  
    else:
        
        for r in range(N):  
            A[r][i], A[r][j] = A[r][j], A[r][i]  
            for c in range(col_cnt):  
                print(A[r][c], end="")  
            print("")  

    
    