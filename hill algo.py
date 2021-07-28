import random
#with elements
k = int(input())
m = int(input())
T = int(input())
C = float(input())

n=k*T*m
dis=[]
#taking user input distance matrix
for i in range(0,k*T*m):
    input_st = input()
    userL = input_st.split()
    #a = []
    new_list = [float(j) for j in userL]
    #print(new_list)
    dis.append(new_list)

# generating shops id
s=0
Shops=[]
for i in range(0,m):
    Sh=[]
    for j in range(0,k*T):
        Sh.append(s)
        s=s+1
    Shops.append(Sh)
x=0
S=0
D=0
G=0
#finding goodness
for i in range(0,T):
    A=[]
    for p in range(0,m):
        for q in range(x,x+k):
            A.append(Shops[p][q])
    c=1
    N=k
    for l in A:
        for l2 in A[c:N]:
            S=S+1-dis[l][l2]
        if c==k:
            c=k+1
            N=N+k
        else:
             c=c+1
    x=x+k
    for l in A[0:k]:
        for l2 in A[k:k+k]:
            D=D+dis[l][l2]
G=S+C*D

max=G
Type=Shops
#solving for 1000 times schedules
for R in range(0,1000):
    a = []
    for i in range(0,k*T*m):
        a.append(i)
    random.shuffle(a)
    Shops = []
    c = 0
    c1 = k * T
    for i in range(0, m):
        k1 = []
        for j in a[c:c1]:
            k1.append(j)
        Shops.append(k1)
        c =c+k*T
        c1 = c + k * T
    x = 0
    S = 0
    D = 0
    G1=0
    for i in range(0, T):
        A = []
        for p in range(0, m):
            for q in range(x, x + k):
                A.append(Shops[p][q])
        #print("A", A)
        c = 1
        N = k
        for l in A:
            # print("l",l)
            # print("slice",A[c:N])
            for l2 in A[c:N]:
                # print("l",l,l2)
                # print("d",dis[l][l2])
                S = S + 1 - dis[l][l2]
                # print("s",S)
            if c == k:
                c = k + 1
                N = N + k
            else:
                c = c + 1
        x = x + k
        for l in A[0:k]:
            # print("a",A)
            for l2 in A[k:k + k]:
                D = D + dis[l][l2]
                # print("dis",D)
        #print("s,d", S, D)
    G1=S+C*D
    #print("G1", S + C * D)
    if G1>max:
        min=G1
        Type=Shops

#print("max",max)
j2=0
c=0
#printing best shops schedule
for i in range(0,m):
    x4 = 0
    x5 = k
    for j in range(0,T):
        for j1 in range(x4,x5):
            #print("index",i,j1)
            print(Type[i][j1]+1,end=" ")
         #   j2+=1
        if n!=4 and x5!=k*T:
             print("|",end=" ")
        c+=1
        x4=x4+k
        x5=x5+k
    print()
    c=0