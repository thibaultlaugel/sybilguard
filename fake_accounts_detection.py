import pickle
import time
import math
Caltech_file=open('Caltech36', 'rb')
F=pickle.load(Caltech_file)
#F=Caltech




###Construction of the detection algorithm

#matrix of friend lists
def friends(A):
    n=len(A)
    B=[[-1 for i in range(n)] for j in range(n)]
    
    t=0
    for i in range(n):
        for j in range(n):
            if (A[i])[j]==1 and (i<j or j>i):
                (B[i])[t]=j
                t=t+1
        t=0
    return B

#s= friends(F)

#degree of the node
def degre (A,i):
    n=len(A)
    t=0
    B=friends(A)
    while (B[i])[t]!=(-1) and t<n:
        t=t+1
    return t

#average node degree of the network
def degremoyen(A):
        n=len(A)
        s=0
        for i in range(n):
                s+=degre(A,i)
        return float(s)/float(n)
                
#Computation of the permutations for each node list
import random
def tablederoutage (A,B):
    n=len(B[0])
    t=[[B[k][l] for k in range(n)] for l in range(n)]
    
    for i in range(n):
        print(100*float(i)/float(n))
        d = degre(A,i)
        for j in range(d):
            k = random.randint(0, d - j)
            t[i][j],t[i][k+j] = t[i][k+j],t[i][j]
    return t

#associate each node to its permutation
def tableroutage2 (A,B,C, node):
    d=degre(A,node)
    RT=[[0 for i in range(d)] for j in range(2)]
    for i in range(d):
        (RT[0])[i]=(B[node])[i]
        (RT[1])[i]=(C[node])[i]
    return RT

def search(B,row,friend):
    n=len(B[0])
    i=0
    while i<n and (B[row])[i]!=friend:
        i=i+1
    if i==n:
        i=0
    return i
    
#image of each node by these permutations at a certain step
def next2(B, RT, friend):
    n=len(RT[0])
    j=0
    while  j<n and B[friend][j]!=friend:        
        j=j+1
    if j>n-1:
        return -1
    else:
        return (RT[friend])[j]





###Construction of the random routes and cromparison

#matrix in which every coefficient ai,j corresponds to the number of the final step of a route starting 
#at the node node and going to the node j, after i permutations
def witness(A,B,RT,node,w):
    n=degre(A,node)
    l=len(A)
    WT=[[0 for h in range(n)] for f in range(w)]
    for i in range(n):
        (WT[0])[i]=node
    for i in range(n):
        (WT[1])[i]=(B[node])[i]
    for i in range(2,w):
        for j in range(n):
            WT[i][j]=next2(B,RT,WT[i-1][j])
    return WT

#Comparison between two random routes 
def comp (A,B,RT,V,S,W):
    cou=witness(A,B,RT,V,W)
    cou2=witness(A,B,RT,S,W)
    d=0
    n=len(cou[0])
    p=len(cou2[0])
    
    for i1 in range(0,n):
        c4=0
        for j1 in range(W):
            for i2 in range(p):
                for j2 in range(W):
                    if (cou[j1])[i1]==(cou2[j2])[i2]:
                        c4=c4+1
        if c4>0:
            d=d+1
    return d





###Defining a detection criterion


###Construction of a random adjacency matrix to train the model

#returns a vector v, which i_th coordinate is equal to the number of nodes that have a degree equal to i
def statistique (A):
        n=len (A)
        v=[0 for s in range (0,n)]
        for i in xrange (0,n):
                v[degre(A,i)]+=1
                print(100*float(i)/float(n))
        return v

#plot the graph
#n=len(F)
#t = arange(0.0,n, 1)
#h=log(t)
y=statistique(F)
#print y[1], y[n-1]

v=np.zeros(n)
for i in xrange(n):
    v[i]=y[i]
print v[1], v[n-1]    
q=log(v)   
plot(h,q)   
show()        
        
#returns a vector which ith coordinate is equal to the sum of the images of the i first integers by f.
def somme (f,n):
    c=0
    v=[0.0 for i in range(n)]
    for i in xrange(1,n):
        v[i]=f(i)+v[i-1]
    return v
    
#definition of the function modeling the number of nodes by degree
def f(i):
    if i==0:
        c=0.0
    else:
        c=0.25*1000*(math.exp(-0.75*math.log(i*(1+math.exp(-math.log(0.75/35)/i)))))
    return c
n=len(F)
v=somme(f,n)

#computes a random node degree, according to the probability distribution associated with the function f.
def prob(v):
    n=len(v)
    c=n
    d=random.random()
    
    for i in range(n-1):
        if  ((v[i])/v[n-1])<=d<((v[i+1])/v[n-1]):
            
            c= i
       
    return c

#random adjacency matrix similar to the Caltech one (same size, similar “number of nodes of a given degree” profile)
def matricerandom2(A,v):
    n=len(A)
    B=[[0 for x in range(n)]for w in range(n)]
    for i in xrange(n):
        h=prob(v)
        print(100*float(i)/float(n))
        g=[0 for s in range(h)]
        for f in range(h):
            s=random.randint(0,n)
            if s<>i :
                g[f]=s
            else :
                g[f]=random.randint(0,n)            
        for j in xrange(i):
            if j in g:
                B[i][j]=1
    for i in xrange(n):
        for j in xrange(i,n):
                              B[i][j]=B[j][i]
        B[i][i]=1
                              
    return B

#plot the graph of the new matrix
C=matricerandom2(F,v)
t = range(0.0,n, 1)
#h=log(t)
y=statistique(C)
v=np.zeros(n)
for i in xrange(n):
    v[i]=y[i]
    t[i]=i
   
plot(t,v)   
show()





###Generation of a random sybil attack

#generation of an exponential probability distribution
def k(v):
    d=random.random()
    s=(math.log(1-d)/v)
    return -s

#which nodes will link the two networks
def generation( n,f):
     c=[[(i,j) for i  in range(f)]for j  in range(n)]
     
     for i in xrange(f):
        
        for j in xrange(n):
            
            k = random.randint(0, n - j-1)
            
            c[j][i],c[k+j][i] = c[k+j][i],c[j][i]
     return  c

#linking the two networks (sybils+ new generated matrix)
def ajoute(A):
    n=len(A)
    f=k(0.1)
    s=k(1)
    if f>=n : #first probability is very low
        f=n-1
    if s>=n :
        s=n-1
    f=int(f)+1 #at least one sybil node
    s=int(s)
    G=generation(n,f)
    V=[[0 for i in range(f)]for j in range(n)]
    for i in xrange(f):
        for j in xrange(s+1):#+1 because we want at least one connection
            (a,b)=G[j][i]
            V[b][a]=1
    for i in xrange(n):
        A[i]=A[i] +V[i]
    for j in xrange(f):
        b=[0 for s in range(n+f)]
        for g in xrange(n):
            if A[g][n+j]==1:
                b[g]=1
        for g in xrange(n+1,n+f):
            b[g]=1
        A=A+ [b]
    return A
D=ajoute(C)

#list of the different number of intersections between the routes of two nodes
def listpour (A,v,s,m):
    B=[0 for i in range (m)]
    Q=friends(A)
    q=tablederoutage(A,Q)
    n=len(A)
    w=int(math.sqrt(n)*math.log(n))
    g=A
    h=A
    d=Q
    c=Q
    j=q
    l=q
    for s in xrange(m):
        B[s]=comp(g,d,j,v,s,w)
        g=h
        d=c
        j=l
        
    return B
    
#empirical expectation of the previous function
def estimation (A,v,s,m):
    V=listpour(A,v,s,m)
    s=somme2(V,m)
    return s/m

#Confusion matrix (number of honest/sybil nodes detected as honest/sybil
def houbre(D,v,s,x):
    f=friends(D)
    B=tablederoutage(D,f)
    n=769
    k=len(D)
    print k
    w=int(math.sqrt(k)*math.log(k))
    J=[[0 for q in range(2)]for d in range(2)]
    xou=[comp(D,f,B,i,s,w) for i  in range(k-n)]
    xou2=[comp(D,f,B,i,s,w) for  i in range(n,k)]
    print xou,xou2
    for i in xrange((k-n)):# on va pas tous les prendre car ça serait bien trop couteux en terme de complexité.mais comme c'est créer aléatoirement ce n'est pas grave 
        print float(i)*float(100)/float (2*(k-n))
        if xou[i]==x:
            J[0][0]=J[0][0]+1
        if xou[i]>x:
            J[0][0]=J[0][0]+1
        if xou[i]<x:
            J[0][1]=J[0][1]+1
    for i in xrange(k-n):
        print float(i)*float(100)/float (2*(k-n))
        if xou2[i]==x:
            J[1][1]=J[1][1]+1
        if xou2[i]>x:
            J[1][0]=J[1][0]+1
        if  xou2[i] < x:
            J[1][1]=J[1][1]+1
    return J




###Results

#True if node is sybil (sybil detected as sybil), False if node is honest (honest detected as sybil
def resul(A,v,s,ve):
    n=len(A)
    verite=False
   
    Fr=friends(A)
    RT=tablederoutage(A,Fr)
    w=int(math.sqrt(n)*math.log(n))
    r=estimation(A,ve,s,m)
    if r<50:
        verite=True
    return verite

    
