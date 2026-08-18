#수프밍1주차-6주차
#중간고사 퀴즈/중간고사 형식=>각 문제당 파일 1개/파일명은 띄어쓰기 없이 영어+숫자 조합/ 확장자는 .py만 가능/ 모듈,생성형 AI 사용 금지/코드 길이 100줄 이내
#2주차
#벡터의 기본 연산(같은 벡터, 덧셈과뺄셈, 내적, 외적)
#행렬의 기본 연산(같은 행렬, 행렬 덧셈과뺄셈, 행렬곱)
#v=[1,-2,3,5]-->이런형태로 벡터 정의해주기

import random  #랜덤한 백터 모두 가져와랏!

def gen_vec(n,a): #함수 선언 그냥 f로 적지말구!()에는 범위 설정해주기
    ret = []
    for _ in range(n):
        ret.append(random.randrange(-a,a+1))
    return ret

def gen_vec_2(n,a):
    ret=[] #안되는 애
    for i in range(n):
        ret[i]=random.randrange(-a,a+1)
    return ret

def gen_zero_vec(n):
    ret = [0]*n
    return ret

#행렬
v=gen_vec(3,4) #v=[,,,]
print("v dimension:", len(v))

def gen_zero_mat(m,n):
    ret=[]  #빈공간 mxn
    #3x2 ret=[[0,0],[0,0],[0,0]]
    for _ in range(m):
        v = gen_zero_vec(n)
        ret.append(v)
    return ret
#print(gen_zero_mat(3,2)) 해주면 출력완!

def gen_identity_mat(n):
    I=gen_zero_mat(n,n)
    for i in range(n):
        I[i][i]=1
    return I


def gen_diag_mat(diagonal):
    """주어진 리스트를 주대각선으로 가지는 정방행렬을 생성한다."""
    n = len(diagonal)
    ret = gen_zero_mat(n, n)
    for i in range(n):
        ret[i][i] = diagonal[i]
    return ret

#행?, 열?
def is_same_mat(A,B):
    #행?
    if len(A)!=len(B):
        return 0
    #열?
    if len(A[0])!=len(B[0]):
        return 0
    rowA = len(A)
    colA = len(A[0])
    for i in range(rowA):
        for j in range(colA):
            if A[i][j]!=B[i][j]:
                return 0
            
    return 1

def new_func(j):
    return j

def mat_add(A,B):  #덧셈이 정의 되는지?
    if len(A)!=len(B): #행이 같은지?
        return 0
    if len(A[0])!=len(B[0]):
        return 0
    #크기가 같음 더할 수 는 있음
    rowA = len(A)
    colA = len(A[0])
    C = gen_zero_mat(rowA,colA)
    for i in range(rowA):
        for j in range(colA):
            C[i][j] = A[i][j]+B[i][j]
    return C

  

def mat_mul(A,B):  #A의 열 ! = B행 =>못함!
    if len(A[0])!=len(B):
        return 0
    rowA = len(A)
    colA = len(A[0])
    colB = len(B[0])
    #C<- rowA x col B
    C = gen_zero_mat(rowA, colB)
    for i in range(rowA):
        for j in range(colB):
            for k in range(colA):
                C[i][j]=C[i][j]+A[i][k]*B[k][j]
    return C

def gen_Mij(A,j):
    ret = gen_zero_mat(len(A)-1, len(A)-1)
    for i in range(1, len(A)):
        for k in range(0, len(A[0])):
            if k<j:
                ret[i-1][k]=A[i][k]
            elif k>j:
                ret[i-1][k-1]=A[i][k]
    return ret


#3주차 
#행렬식을 계산하고 구현
#가우스 소거법을 이해하고 구현
#det(A)=0 인 행렬의 경우 (1.영역의 크기가 사라짐 2. Dimension이 낮아짐 3. 역행렬 없음)

def det_2x2(A):
    return A[0][0]*A[1][1]-A[0][1]*A[1][0]

def det_nxn(A):
    rowA = len(A)
    colA = len(A[0])
    if rowA!=colA:
        return
    # A는 nxn 행렬
    if rowA==2: #A는 2x2
        return det_2x2(A)
    else: #nxn 계산 덧셈에 대한 누적이니까 ret=0으로 초기화 시켜줌
        ret = 0 #ret=ret+a11c11 ...결론적으로 우리가 원하는 누적값을 얻을 수 있음.
        for i in range(colA):
            sign = (-1)**i #A[0][i]
            Asub = gen_Mij(A,i)
            print(Asub)
            ret += sign*A[0][i]*det_nxn(Asub)
        return ret
    
#Gaussian Elimination
#행렬의 역행렬 찾기 가능, 효율적인 행렬식 연산 가능, 행렬의 행/열 공간 찾기 가능
#Input: 행렬 A Output: reduced row-echelon form of A
#Algorithm=Row모두 탐색>0번째 column부터 Pivot 확인
#행렬 복사를 하는 이유 복사본으로 해야지 훼손이 안됨!!

def copy_mat(A):
    rowA=len(A)
    colA=len(A[0])
    Acpy = gen_zero_mat(rowA, colA)
    for i in range(rowA):
        for j in range(colA):
            Acpy[i][j]=A[i][j]
    return Acpy
    
def swap_row(A,i,j):
        tmp=[] # A의 i열 저장할 임시공간!
        for nc in range(len(A[0])):
            tmp.append(A[i][nc])
        for nc in range(len(A[0])):
            A[i][nc]=A[j][nc]
        for nc in range(len(A[0])):
            A[j][nc] = tmp[nc]
            
def gaussian_elim(A):
        rowA = len(A)
        colA = len(A[0])
        Acpy = copy_mat(A)
        
        pr =0 #pivot row
        pc =0 #pivot col
        while pr<rowA and pc <colA:
            i = pr
            while Acpy[i][pc]==0 and i+1<rowA:
                i=i+1
            if Acpy[i][pc]==0 and i+1==rowA:  #이 열은 다 0임
                pc = pc+1
            else: #이 열에 0이 아닌애가 있음
                swap_row(Acpy,i,pr)
                k = Acpy[pr][pc]
                
                for j in range(colA):
                    Acpy[pr][j] = Acpy[pr][j]/k #pivot을 1로 만든다
                    
                for j in range(pr+1, rowA): #pivot 아래를 0으로 만든다
                    k = Acpy[j][pc]
                    for l in range(pc, colA):
                        Acpy[j][1]=Acpy[j][l]-k*Acpy[pr][1]
                        
                pr = pr+1
                pc = pc+1   #계속 반복~
        return Acpy

#4주차
#Gauss-Jordan Elimination
#가우스 소거법 vs. 가우스=요르단 소거법 : 전진단계 수행/ 선도 1아래 부분을 모두 0으로 하는 행 사다리꼴//전진+후진단계 수행/ 기약행사다리꼴로 변형
#기본 행렬과 AA-1=I 로 구하기

#실습: 역행렬 구하는 함수 구하기 function name: mat_inv
#Input: 행렬A
#Output: A-1(정방행렬 아니면 None 출력/구할 수 없으면 None 출력)

def gj_elim(A):
    rowA = len(A)
    colA = len(A[0])
    Acpy = copy_mat(A)
    
    pr = 0
    pc = 0
    while pr<rowA and pc<colA:
        i = pr
        while round(Acpy[i][pc])==0 and i+1<rowA:
            i = i+1
        if round(Acpy[i][pc])==0 and i+1==rowA:     #round가 뭐임?
            pc = pc+1
        else:
             swap_row(Acpy,i,pr)
             k = Acpy[pr][pc]
             for j in range(pc, colA): #pivot 위에도 다 0으로 쳐 발라야되니까 g,gj 차이점!
                 Acpy[pr][j] = Acpy[pr][j]/k  #pivot을 1로 변화
                 
             for j in range(rowA):
                if j == pr:
                    continue
                
                k = Acpy[j][pc]
                for l in range(colA):
                    Acpy[j][l]=Acpy[j][l]-k*Acpy[pr][l]
                    
             pr = pr+1
             pc = pc+1
        
    return Acpy
            
def ext_mat(A, rowA): #AㅣI
    ret = gen_zero_mat(rowA,rowA<<1)          
    for i in range(rowA):
        for j in range(rowA):
            ret[i][j] = A[i][j]
        ret[i][rowA+i]=1
    return ret         

def mat_inv(A):
    rowA=len(A)
    colA=len(A[0])
    if rowA!=colA:
        return
    #Acpy <-AㅣI
    Acpy = ext_mat(A,rowA)
    
    
    #gj
    pr = 0
    pc = 0 #초기화시키기
    while pr<rowA and pc<colA:
        i = pr
        while round(Acpy[i][pc])==0 and i+1<rowA:  #여기 round를 추가하는 이유?
            i = i+1
        if round(Acpy[i][pc])==0 and i+1==rowA:  #역행렬이 존재할 수 없음
            return
        
        swap_row(Acpy,i,pr) #올리는것임
        k = Acpy[pr][pc]
        for j in range(pc,colA<<1):
            Acpy[pr][j] = Acpy[pr][j]/k #pivot1
            
            # pr 위 아래 성분 제거하기<-여기가 gj소거 하는 부분임!
        for j in range(rowA):
            if j == pr:
                continue
                
            k = Acpy[j][pc]
            for l in range(colA<<1):
                Acpy[j][l] = Acpy[j][l]-k*Acpy[pr][l]
        pr = pr+1
        pc = pc+1
            
           #Acpy = [IㅣA-1] 
        Ainv = gen_zero_mat(rowA, colA)
        
        for i in range(rowA):
            for j in range(colA):
                Ainv[i][j] = Acpy[i][j+colA]
                
        return Ainv
            
            
            
#5주차

#고유값/고유벡터
#고유벡터와 고유값에 대한 정의를 알기>2*2 행렬에 대한 고유값과 고유벡터 구하는 함수 구현
#Power Iteration Method 알기>이걸로 고유값과 고유벡터 찾기
#행렬에 벡터를 곱했을때 Ax=3x 처럼 실수배 가능하면 3이 고유값이 되는것
#특성 방정식: det(ㅅI-A)=0를 만족하면 됨. Ax=ㅅx 을 이항해서 도출해낸것 yk
#역행렬이 없어야한다!!=detB=0 을 만족하는 ㅅ(람다)를 찾아야하는것!
#step1: 고유값찾기>step2: 고유벡터 찾기
#A가 n*n삼각행렬(상삼각,하삼각,대각)이면 A의 고유값은 A의 주대각선상의 원소이다.

#실습 1
#행렬(n*n)과 값(ㅅ)을 입력 받아, 주어진 값이 고유값인지 아닌지 확인하는 함수를 만드시오
#Input: 행렬, 값(scalar)
#Output: 고유값인지의 여부
def is_eigen_val(A,b):
    nrow = len(A)
    B = copy_mat(A)
    for i in range(nrow):
        B[i][i]=B[i][i]-b
    #B=A-bI
    ret = det_nxn(B)
    if ret ==0:
        return 1
    else:
        return 0
    
def mat_vec_mul(A,x):
    nrow = len(A)
    ncol = len(A[0])
    Ax = [[0] for _ in range(nrow)]
    for i in range(nrow):
        for k in range(ncol):
            Ax[i][0] = Ax[i][0]+A[i][k]*x[k]
    return Ax   
        
def is_eigen_vec(A,x):
    Ax = mat_vec_mul(A,x)
    nrow = len(x)
    k = Ax[0][0]/x[0]
    for i in range(1,nrow):
        if x[i][0]*k != Ax[i][0]:
            return 0
    return 1

#실습 2
#2*2 행렬의 고유값 구하기
#Input: 행렬 A
#Output: 고유값
#Hint: 근의 공식 이용

def eigen_2x2(A):
    a=A[0][0]
    b=A[0][1]
    c=A[1][0]
    d=A[1][1]
    
    D = (a+d)**2-4*(a*d-b*c)
    D = D**(1/2)
    
    k1 = ((a+d)+D)/2
    k2 = ((a+d)-D)/2
    return k1, k2

#실습 3
#2*2 행렬의 고유벡터 구하기
#Input: 행렬 A, 고유값 n
#Output: 고유벡터
#Hint: 이차방정식의 해 이용, 주어진 값이 고유값이 아닐 경우 오류 출력하기

def eigvec_2x2(A):
    k1, k2 = eigen_2x2(A)
    
    v1=[A[0][1], k1-A[0][0]]
    v2=[A[0][1], k2-A[0][0]]
    
    return k1, k2, v1, v2

#power iteration method(=거든제곱법)
#(사람)특성방정식 이용 (컴퓨터) 방정식 푸는것은 특성방정식 쓸 수가 없음.->행렬 벡터 연산은 쉬움
#Av=ㅅv 에서 v가 ㅅ(람다)배 늘어남. 근데 여기서 람다를 계속 곱하게 되면 우세한 고유값에 수렴하게 된다.

#열벡터 복사 함수
def copy_vec(x):
    nrow = len(x)
    ret =[[0] for _ in range(nrow)]
    for i in range(nrow):
        ret[i][0]=x[i][0]
    return ret

def diff_vec(v,w):
    #크기 구하기(제곱해서 더하고 루트씌우는 과정)
    nrow = len(v)
    u=[[0] for _ in range(nrow)]
    for i in range(nrow):
        u[i][0]=v[i][0]-w[i][0]
        
    #u=v-w
    ret=0
    for i in range(nrow):
        ret = ret+ (u[i][0]*u[i][0])
    ret = ret**(1/2)
    return ret
#행<->열 벡터 바꾸기 그리고 크기구하기

def rowvec_to_colvec(rv):
    nrow = len(rv)
    cv = [[0]for _ in range(nrow)]
    for i in range(nrow):
        cv[i][0]=rv[i]
    return cv

def colvec_to_rowvec(cv):
    nrow = len(cv)
    rv=[0]*nrow
    for i in range(nrow):
        rv[i]=cv[i][0]
    return rv

def unit_col_vec(u):
    nrow = len(u)
    uv = [[0] for _ in range(nrow)] #for in range문 ? for while 문, if els 문 정리하기
    #벡터 크기 계산
    ret=0
    for i in range(nrow):
        ret = ret + (u[i][0]*u[i][0])
    ret = ret**(1/2)
    
    for i in range(nrow):
        uv[i][0]=u[i][0]/ret
        
    return uv #단위 컬럼 벡터 완성!

def colvec_dot(v,w):
    ret=0
    for i in range(len(v)):
        ret = ret + v[i][0]*w[i][0]
    return ret

def pim(A,iter,diff,max_cnt):
    flag=0
    cnt=0
    rowA = len(A)
    while flag==0:
        v = gen_vec(rowA,10)
        v = rowvec_to_colvec(v)
        v = unit_col_vec(v)
        t = copy_vec(v)
        
        for i in range(iter):
            v = mat_vec_mul(A,v) #A,v
            v = unit_col_vec(v) 
            delta = diff_vec(v,t)
            t = copy_vec(v)
        cnt = cnt+1
        
        if delta<diff:
            flag =1
        if cnt>=max_cnt:
            return
        
        #찾음!
        Av = mat_vec_mul(A,v)
        Av_v = colvec_dot(Av,v)
        v_v = colvec_dot(v,v)
        k = Av_v/v_v
        return v, k
    

#6주차(최종 목표!!)
#행렬 분해하는 방법(2*2 행렬, n*n 행렬 QR분해)=>in order to undestand basic thing&efficient calculation
#Matrix decomposition( Eigen decomposition(Only 정사각행렬), LU decomposition, QR decomposition(열이서로독립)=>det=1인것들)
#Eigen decomposition(only 2*2 matrix구현할거임=>대각화 가능할때 P-1AP=D)
#실습 1: 대각화 하는 방법(일반적인 곱셈으로 An vs. eigen decomposition으로 An 구하기)

A= [[6, -1], [2,3]]

def inv_2x2(A):
    Ainv = gen_zero_mat(2,2)
    Ainv[0][0]=A[1][1]
    Ainv[0][1]=-A[0][1]
    Ainv[1][0]=-A[1][0]
    Ainv[1][1]=A[0][0]
    
    det = det_2x2(A)
    for i in range(2):
        for j in range(2):
            Ainv[i][j]=Ainv[i][j]/det
    return Ainv


def diag_2x2(A):
    k1, k2, v1, v2 = eigvec_2x2(A)
    D = gen_zero_mat(2,2)
    P = gen_zero_mat(2,2)
    
    D[0][0]=k1
    D[1][1]=k2
      
    P[0][0] = v1[0][0]
    P[1][0] = v1[1][0]
    P[0][1] = v2[0][0]
    P[1][1] = v2[1][0]

    Pinv = inv_2x2(P)
    
    return P, D, Pinv

#QR decomposition 
#Gram-Schmidt process(서로 독립인 벡터> 서로 직교하는 벡터 proju(v)!!)

#A^T
def mat_trans(A):
    nrow = len(A)
    ncol = len(A[0])
    AT = gen_zero_mat(ncol, nrow)
    
    for i in range(nrow):
        for j in range(ncol):
            AT[j][i]=A[i][j]
    return AT
#정사영 퀴즈나옴!!

def unit_row_vec(v):
    uv = [0]*len(v)
    ret = 0
    for i in range(len(v)):
        ret = ret + v[i]*v[i]
    ret = ret**(1/2)
    
    for i in range(len(v)):
        uv[i]=v[i]/ret
        
    return uv #단위 행 벡터 완성 proju(v)

def rowvec_dot(u,v):
    udv=0
    for i in range(len(u)):
        udv = udv + u[i]*v[i]
    return udv

def proj_uv(u,v):
    udv = rowvec_dot(u,v)
    udu = rowvec_dot(u,u)
    k = udv/udu 
    ret = [0]*len(v)
    for i in range(len(v)):
        ret[i]=u[i]*k
        
    return ret

#행벡터 형태, u-v
def rowvec_sub(u,v):
    ret = [0]*len(u)
    for i in range(len(u)):
        ret[i]=u[i]-v[i]
    return ret

def copy_row(u):
    ret = [0]*len(u)
    for i in range(len(u)):
        ret[i]=u[i]
    return ret


def gram_schmidt(A):
    rowA = len(A)
    AT = mat_trans(A)
    
    for i in range(1, rowA):
        ri = copy_row(AT[i])
        for j in range(0, i):
            tmp = proj_uv(AT[j],ri)
            AT[i] = rowvec_sub(AT[i], tmp)
    
    for i in range(rowA):
        AT[i] = unit_row_vec(AT[i])
        
    ret = mat_trans(AT)
    return ret

def QR_decompose(A):
    nrow = len(A)
    Q = gram_schmidt(A)
    R = gen_zero_mat(nrow,nrow)
    
    AT = mat_trans(A) #A transpose라는 뜻임!
    QT = mat_trans(Q)
    
    for i in range(nrow):
        for j in range(i+1):
            R[j][i]=rowvec_dot(AT[i],QT[j])
    return Q, R

def solve_vec(A):
    nrow = len(A)
    ncol = len(A[0])
    
    pv=[]
    for i in range(nrow):
        for j in range(ncol):
            if round(A[i][j])==1:
                pv.append(j)
                break
            
    fv =  [j for j in range(ncol) if j not in pv]
    
    v=[]
    nsol = len(fv)
    #print("pivot:", pv)
    #print("free variable:", fv)
    
    #해를 담을 공간 설정
    for i in range(0, nsol):
        a=[0]*ncol
        v.append(a)
    
    #free variable에 1넣기
    for i in range(0, nsol):
        v[i][fv[i]]=1
        
    #해 구하기
    for rnd in range(nsol):
        for i in range(nrow-1, -1, -1):
            if i<len(pv):
                pc = pv[i]
                tmp=0
                for j in range(pc+1, ncol):
                    tmp = tmp + A[i][j]*v[rnd][j]
                    
                v[rnd][pc]= -tmp
                
    return v, nsol

        
        
    
#QR 분해로 eigenvalue, eigenvector 구하기
#(A-ㅅI)x=0의 해 구하기 nxn이 input이기 때문에 최대 n개의 고유값,고유벡터 구할 수 있음=>걍 방정식 풀듯이 풀면됨

def eig_nxn(A):
    nrow = len(A)
    Acpy = copy_mat(A)
    
    #STEP1 : eigenvalue 구하기
    for i in range(100): #100번 반복
        Q, R = QR_decompose(Acpy)
        Acpy = mat_mul(R,Q) #A1=R*Q
        
    #STEP2 : eigenvalue 구하기
    val=[]
    vec=[]
    mul=[]
    
    for i in range(nrow):
        if round(Acpy[i][i]) not in val:
            val.append(round(Acpy[i][i]))
            mul.append(1)
        else:
            idx =val.index(round(Acpy[i][i]))
            mul[idx]=mul[idx]+1
            
            
    print("val:", val)
    print("mul:", mul)
    
    #STEP3 : eigenvector 구하기
    for i in range(0,len(val)):
        B= copy_mat(A)
        
        #B=A-ㅅI
        for j in range(nrow):
            B[j][j]=B[j][j]-val[i]
            
        B = gj_elim(B)
        #Bv=0이 되는 v 구하기
        v, nsol = solve_vec(B)
        a=[]
        for j in range(nsol):
            a.append(v[j])
        vec.append(a)
    return val,mul,vec
        
    
    
    
    



            
    

############################테스트!!#################################

#2주차 행렬식 test
A = gen_zero_mat(3,4)
print(A)
print("A row(행):", len(A))
print("A col(열):", len(A[0]))
print(gen_identity_mat(3))

A=[[1,2], [3,4], [5,6]] #3x2
B=[[1,2], [3,4]]
C=[[1,2], [3,4], [5,5]] #3x2
D=[[1,2], [3,4], [5,6]]

print(is_same_mat(A,B)) #답=0
print(is_same_mat(A,C)) #답=0
print(is_same_mat(A,D)) #답=1
    
print(mat_add(A,B)) #답=0
print(mat_add(A,C))    

A=[[1,2]]
B=[[1,0,1], [2,1,-1]]
C=[[2,3]]

print(mat_mul(A,C))
print(mat_mul(A,B))

#3주차 행렬식 test
A=[[3,1,-4], [2,5,6], [1,4,8]]
print("det A:",det_nxn(A))

A=[[2,4,-3], [5,10,-7], [3,6,5]] #A'=[[2,4,-3], [0,0,1], [0,0,0]] ~가우스 잘 된 결과임
Ap = gaussian_elim(A)
Aj = gj_elim(A)

print("A:", A)
print("Ap:", Ap)
print("Aj:", Aj)

#4주차 행렬식 test

print("mat inv:", mat_inv(A)) #여기까지 일단 확장은 잘 되었구나 확인
B=[[3,-2,4],[1,0,2],[0,1,0]]
print("mat inv B:", mat_inv(B))


Binv = mat_inv(B)
print("B*B^-1:", mat_mul(B,Binv))

#5주차 고유값 test
A=[[6,-1], [2,3]] #5,4

print("is 5 eigenvalue? : ", is_eigen_val(A,5)) 
print("is 4 eigenvalue? : ", is_eigen_val(A,4))
print("is 3 eigenvalue? : ", is_eigen_val(A,3))
print("is 2 eigenvalue? : ", is_eigen_val(A,2))

x1 = [1, -1]   # ✅ 이렇게 1차원 리스트로 정의
x2 = [1, 1]
x3 = [1, 2]

print("is x1 eigenvec?:", is_eigen_vec(A,x1)) #답=x
print("is x2 eigenvec?:", is_eigen_vec(A,x2)) #답=0
print("is x3 eigenvec?:", is_eigen_vec(A,x3)) #답=0

print("eigenvalues:", eigen_2x2(A)) #답=5,4

k1, k2, v1, v2 = eigvec_2x2(A)

print("eigenvalue: ", k1, "eigenvector: ", v1)
print("eigenvalue: ", k2, "eigenvector: ", v2)

v,k = pim(A,100,0.001,10)
print("eigenvec:", v)
print("eigenval:", k)

#6주차 행렬식 test

P, D, Pinv = diag_2x2(A)
print("P: ", P)
print("D: ", D)
print("Pinv: ", Pinv)

ret = mat_mul(P,D)
ret = mat_mul(ret,Pinv)
print("PDP^-1:", ret) #A랑 똑같이 나와야함

import time

#A^200
A=[[6,-1], [2,3]] #5,4
B=copy_mat(A)
start = time.time()
for i in range(198):
    B=mat_mul(B,A)
end = time.time()
print("general mul: ", (end-start))

#A^200 = P*D^200*P^-1
start=time.time()
P, D, Pinv = diag_2x2(A)
D[0][0]=D[0][0]**200
D[1][1]=D[1][1]**200
ret = mat_mul(P,D)
ret = mat_mul(ret,Pinv)
end= time.time()
print("DIAG mul: ", (end-start))

#Gram-Schmidt test
A=[1,1,0], [0,1,1], [1,1,1]

gA = gram_schmidt(A)
gAT = mat_trans(gA)

print(mat_mul(gA,gAT))

A=[[3,1,0], [2,0,1]], [1,1,1]
Q, R = QR_decompose(A)

ret = mat_mul(Q,R)
print("QR:", ret)


A=[[6,-1], [2,3]] #5,4
print("====week6 eigenvalue=====")
val, mul, vec=eig_nxn(A)
print("val:", val)
print("mul:", mul)
print("vec:", vec)

B=[[2,-3,0],[2,-5,0],[0,0,3]]
val, mul, vec=eig_nxn(B)
print("val:", val)
print("mul:", mul)
print("vec:", vec)

C=[[5,-10,-5],[2,14,2], [-4,8,6]]
val, mul, vec=eig_nxn(C)
print("val:", val)
print("mul:", mul)
print("vec:", vec) #//


D=[[1,0,0], [0,1,3], [0,0,0]]
v, nsol=solve_vec(D)
print("v: ", v)
print("nsol: ", nsol)

E=[[1,-1,3], [0,0,0], [0,0,0]]
v, nsol=solve_vec(E)
print("v: ", v)
print("nsol: ", nsol)



