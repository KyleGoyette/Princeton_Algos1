__author__ = 'Kyle'
import random
import numpy
numpy.set_printoptions(threshold='nan')
data=[]
with open('testcut.txt','r') as f:
    data = [map(int, line.split()) for line in f]


z= [len(data),len(data)]
a=numpy.zeros(z)

for i in range(0,len(data)):
    for j in range(1,len(data[i])):
        a[i,data[i][j]-1]=1
a=numpy.matrix(a)

def contraction(a,n):
    numpy.random.seed()
    random.seed()
    b=numpy.matrix(a)+1-1
    mini=numpy.shape(a)[0]
    for k in range(0,n^2):
        a=b+1-1
        while numpy.shape(a)[0] > 2:
            x,y=numpy.nonzero(a)
            i=random.randint(0,numpy.shape(x[0])[1]-1)       #x[0,i] is node1-1 and y[0,i] is node2-1
            contnode=x[0,i]
            tonode=y[0,i]
            for j in range(0,numpy.shape(a)[0]):
                if (tonode!=j):
                    a[tonode,j]+=a[contnode,j]
                    a[j,tonode]+=a[contnode,j]
            a=numpy.delete(a,contnode,axis=0)
            a=numpy.delete(a,contnode,axis=1)
        if a[0,1]<mini:
            mini=a[0,1]
    print a
    return mini

print contraction(a,20)