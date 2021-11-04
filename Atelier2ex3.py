list=[11,45,8,11,23,45,23,45,89]
dict={}
def frequency(n, list):
    count = 0
    for k in list:
        if k == n :
            count+=1
    return count

for i in range(0,len(list)):
    n=list[i]
    print(frequency(n,list))
