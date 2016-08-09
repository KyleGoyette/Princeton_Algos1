__author__ = 'Kyle'
n=[4,3,2,1]
count=0

def inversioncountandsort(n,count):
    if len(n)<2:
        return n,count
    elif len(n)>1:
        result=[0]*len(n)
        mid=int(len(n)/2)
        y=inversioncountandsort(n[:mid],count)
        yc=y[1]
        y=y[0]
        x=inversioncountandsort(n[mid:],count)
        xc=x[1]
        x=x[0]
        count=count+xc+yc
        i=0
        j=0
        k=0
        m=max(x,y)
        for k in range(len(n)):
            if y[i] < x[j]:# and i<(len(y)):
                result[k]=y[i]
                if i<(len(y)-1):
                    i+=1
                else:
                    y[i] = m
                print result
            elif x[j] <= y[i]:
                result[k]=x[j]
                count+=1
                if j<(len(x)-1):
                   j+=1
                else:
                    x[j] = m
    return result,count

print inversioncountandsort(n,count)

z= [len(data),len(data)]
a=numpy.zeros(z)
for i in range(0,len(data)):
    for j in range(1,len(data[i])):
        a[i,data[i][j]-1]=1
#print a[:,0]
print a[0,:]
for i in range(1,200):
    print str(i) + " " +  str(a[199,i])
print numpy.shape(a)