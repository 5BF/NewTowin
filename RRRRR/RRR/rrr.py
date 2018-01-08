import os
a=["ascii"]
print(len(a[0]))

b="qwer"
print(len(b))

listG=["a","b","c",1,2,3]


def listA(lista):
    for listb in lista:
        if isinstance(listb,list):
            listA(listb)
        else:
            print(listb)
            print("1")
listA(listG)

man=[]
other=[]
try:
    fileA = open('C:\\Users\\Administrator\\PycharmProjects\\untitled2\\RRRRR\\RRR.txt', 'r')
    filemsg = fileA.readlines()
    # print(filemsg,end='')

    for F in filemsg:
        (first, second) = F.split(',', 1)
        second=second.strip()
        if first =='MAN':
            man.append(second)
        elif first=='womwn':
            other.append(second)
        #print(first, end='')
        #print(':::::', end='')
        #print(second, end='')
        '''B=F.split(',')[0]
        C=F.split(',')[1]
        print(B,end='')
        print(C,end='')'''
    fileA.close()
except:
    pass
print(man)
print(other)

try:
    A=open('C:\\Users\\Administrator\\PycharmProjects\\untitled2\\RRRRR\\AA.txt', 'w')
    B=open('C:\\Users\\Administrator\\PycharmProjects\\untitled2\\RRRRR\\BB.txt', 'w')
    print(man,file=A)
    print(other,file=B)
    A.close()
    B.close()
except:
    pass





GGG=[]

try:
    with open('C:\\Users\\Administrator\\PycharmProjects\\untitled2\\RRRRR\\666.txt') as A_file:
        dataA=A_file.readline()
        dataB=dataA.strip().split(',')
        GGG.append(dataB)
    '''with open('C:\\Users\\Administrator\\PycharmProjects\\untitled2\\RRRRR\\GGGG.txt') as GG_file:
        GGG.append(dataA)
        print(GGG,file=GG_file)'''
except:
    print("GG")
print(dataA)
print(dataB)
print(GGG)

try:
    with open('C:\\Users\\Administrator\\PycharmProjects\\untitled2\\RRRRR\\GGGG.txt','w') as GG_file:
        #GGG.append(dataA)
        print(GGG,file=GG_file)
except:
    print("ggggggggg")


HHH=[6,5,4,32,1,0]
HHH.sort()
print(HHH)


jjj=[66,55,66,77,111]
JJJ=sorted(jjj)
print(jjj)
print(sorted(JJJ))



kk=[1,2,3,4,5,6,8,7,7]
lll=sorted([m*2 for m in kk])
print(lll)

dis=sorted(set(lll))[0:3]
print(dis)

def sanitize(time_string):
    if '-' in time_string:
        splitter='-'
    elif '.' in time_string:
        splitter='.'
    else:
        return (time_string)
    (mins,secs)=time_string.split(splitter)
    return (mins+'.'+secs)

def get_coach_data(filename):
    try:
        with open(filename) as f:
            data=f.readline()
            return (data.strip().split(','))
    except:
        print('GGGHHH')

yyy2=get_coach_data('C:\\Users\\Administrator\\PycharmProjects\\untitled2\\RRRRR\\s.txt')
name=yyy2.pop(0)
talent=yyy2.pop(0)
print(name+" is "+talent+str(sorted(sanitize(t) for t in yyy2)[0:3]))










