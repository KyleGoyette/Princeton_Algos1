__author__ = 'Kyle'
import sys
sys.setrecursionlimit(999999999)
d={}
drev={}
dnew={}
# with open("Scctest.txt") as f:  IF ALL VALUES FOR ONE KEY ON ONE LINE DO THIS
#     for line in f:
#         (key,val) = line.split(" ",1)
#         d[int(key)] = map(int, val.split())
#         dnew[int(key)]=[]
#         if int(key) not in drev:
#             drev[int(key)]=[]
#         for i in map(int, val.split()):
#             if i in drev:
#                 drev[i].append(int(key))
#             else:
#                 drev[i]=[int(key)]
with open("Scctest.txt") as f:
    for line in f:
        (key,val) = line.split()
        if int(key) not in d:
            d[int(key)] = [int(val)]
            dnew[int(key)]=[]
        else:
            d[int(key)].append(int(val))
        if int(val) not in d:
            d[int(val)]=[]
            dnew[int(val)]=[]

        if int(key) not in drev:
            drev[int(key)]=[]

        if int(val) in drev:
            drev[int(val)].append(int(key))
        else:
            drev[int(val)]=[int(key)]

print len(d)
print len(drev)
print len(dnew)


def dfs_rec1(graph,start,t,f,path = []):
    path = path + [start]
    for edge in graph[start]:
        if edge not in path:
            path,f,t = dfs_rec1(graph,edge,t,f,path)
    t+=1
    f[start-1]=t
    return path,f,t
#Gnew[fin[j[0]-1]]=[fin[j[1][0]-1]]

def dfs_rec2(graph,start,s,sin,path=[]):
    path=path+[start]
    for edge in graph[start]:
        if edge not in path:
            path,sin=dfs_rec2(graph,edge,s,sin,path)
    sin[int(start)-1]=s
    #print sin
    return path,sin

fin=[0]*(len(drev))
t=0
h=[]
for j in range(len(d),1,-1): #determines the new node numbers
    if j not in h:
        h,fin,t=dfs_rec1(drev,j,t,fin,h)
#print G
#print fin

# for i in range(1,len(G)): #creates new G with new node numbers
#     for j in range(0,len(G[i])-1):
#         Gnew[i][j]=fin[G[i][j]-1]
#         print fin[G[i][j]-1]
for j in d.iteritems():
    for i in range(0,len(j[1])):
        dnew[fin[j[0]-1]].append(fin[j[1][i]-1])

hin=[0]*(len(dnew))
h=[]
for i in range(len(d),1,-1):
    if i not in h:
        h,hin=dfs_rec2(dnew,i,i,hin,h)
        #print h
        #print hin
print hin

print len(set(hin))
