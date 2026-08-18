
def copy_mat(A):  
    r = len(A)  
    c = len(A[0]) 
    B = [[0.0 for _ in range(c)] for _ in range(r)] 
    for i in range(r):  
        for j in range(c): 
            B[i][j] = A[i][j] 
    return B 

def swap_row(A, i, j):  
    A[i], A[j] = A[j], A[i]  

def gaussian_elim(A):  
    r = len(A) 
    c = len(A[0])  
    pr = 0  
    pc = 0 

    while pr < r and pc < c:  
        i = pr 
        while i < r and abs(A[i][pc]):
            i += 1  

        if i == r:  
            pc += 1  
            continue 

        if i != pr:  
            swap_row(A, i, pr)  

        piv = A[pr][pc] 
        for j in range(pc, c):  
            A[pr][j] = A[pr][j] / piv 
        
        for rr in range(r): 
            if rr == pr: 
                continue 
            k = A[rr][pc] 
            for jj in range(pc, c): 
                A[rr][jj] = A[rr][jj] - k * A[pr][jj] 

        pr += 1  
        pc += 1 

    return A  

def rank_of(A):  
    R = copy_mat(A)  
    R = gaussian_elim(R)  
    rk = 0  
    for i in range(len(R)): 
        nonzero = 0  
        for j in range(len(R[0])): 
            if abs(R[i][j]):  
                nonzero = 1  
                break  
        rk += nonzero  
    return rk  


N = int(input().strip()) 
A = []  
for _ in range(N): 
    A.append(list(map(int, input().split())))  

print(rank_of(A)) 

