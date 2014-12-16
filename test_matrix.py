####Generation of a random social matrix based on Caltech's matrix

# 1 /
#Calculation of the probability of having two people being friends according to the Caltech matrix
import numpy
import pickle
#print [i for i in xrange(2,4)]
Caltech_file = open('Caltech36', 'rb')
Caltech = pickle.load(Caltech_file)
A=Caltech


def probaamis(A):
    n=len(A)
    u=[0 for i in range(n)]
    m=0
    for i in range(n):
        for j in range(n):
            u[i]=u[i]+A[i][j]/(2*n)
        m=m+u[i]/(n)
    return m

import random


def bernoulli(p):
        a=random.random()
        if a<p:
            return 1
        else:
            return 0



#Creation of the test matrix


def matricerandom(A):
    n=len(A)
    B=[ [ 0 for i in range(n) ] for j in range (n)]
    for i in range(len(A)):
        for j in range(len(A)):
            B[i][j]=bernoulli(probaamis(A))
    return B

matricerandom(A)
