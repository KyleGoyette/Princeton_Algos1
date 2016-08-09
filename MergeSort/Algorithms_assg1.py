__author__ = 'Kyle'
data_array=open('IntegerArray.txt','r')
data=[]
for line in data_array:
    data.append(int(line))


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

x= inversioncountandsort(data,0)
print x[1]
print x[0][99999]