__author__ = 'Kyle'
def Partitionfor(A,l,r):
    count=r-l-1
    p=A[l]
    i=l+1
    for j in range(l+1,r):
        if A[j]<p:
            tmp=A[j]
            A[j]=A[i]
            A[i]=tmp
            i+=1
    tmp=A[l]
    A[l]=A[i-1]
    A[i-1]=tmp
    return i,count

def Partitionback(A,l,r):
    A[r-1],A[l]=A[l],A[r-1]
    count=r-l-1
    p=A[l]
    i=l+1
    for j in range(l+1,r):
        if A[j]<p:
            tmp=A[j]
            A[j]=A[i]
            A[i]=tmp
            i+=1
    tmp=A[l]
    A[l]=A[i-1]
    A[i-1]=tmp
    return i,count

def quickSort(A,p,q):
    count=0
    if p<q:
        r,count=Partitionback(A,p,q)
        count+=quickSort(A,p,r-1)
        count+=quickSort(A,r,q)
    return count

count=0


A=[3,2,5,8,1,9]
quickSort(A,0, len(A))
print A
