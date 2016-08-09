__author__ = 'Kyle'
n=[10,5,3,7,8,2]
count=0

def inversioncountandsort(n,count):
    result=[]
    if len(n)<2:
        return n,count
    elif len(n)>1:
        mid=int(len(n)/2)
        y=inversioncountandsort(n[:mid],count)
        x=inversioncountandsort(n[mid:],count)
        yc=y[1]
        y=y[0]
        xc=x[1]
        x=x[0]
        i=0
        j=0
        k=0
        count=xc+yc+count
        while i<len(y) and j<len(x):
            if y[i] > x[j]:# and i<(len(y)):
                result.append(x[j])
                count+=(len(y)-i)
                j+=1
            else:
                result.append(y[i])
                i+=1
        result+=y[i:]
        result+=x[j:]
    return result,count

print inversioncountandsort(n,count)