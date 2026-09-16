# 66_searching_algorithms.py
# Searching Algorithms - 10 practical programs/features

def linear_search(a,t):
    for i,v in enumerate(a):
        if v==t:return i
    return -1

def binary_search(a,t):
    lo,hi=0,len(a)-1
    while lo<=hi:
        m=(lo+hi)//2
        if a[m]==t:return m
        if a[m]<t:lo=m+1
        else:hi=m-1
    return -1

def first_occurrence(a,t):
    lo,hi,ans=0,len(a)-1,-1
    while lo<=hi:
        m=(lo+hi)//2
        if a[m]==t:ans=m;hi=m-1
        elif a[m]<t:lo=m+1
        else:hi=m-1
    return ans

def last_occurrence(a,t):
    lo,hi,ans=0,len(a)-1,-1
    while lo<=hi:
        m=(lo+hi)//2
        if a[m]==t:ans=m;lo=m+1
        elif a[m]<t:lo=m+1
        else:hi=m-1
    return ans

data=[2,4,4,4,7,9,12]
print('1. Data:',data)
print('2. Linear search 7:',linear_search(data,7))
print('3. Binary search 9:',binary_search(data,9))
print('4. Missing value:',binary_search(data,10))
print('5. First 4:',first_occurrence(data,4))
print('6. Last 4:',last_occurrence(data,4))
print('7. Count 4:',last_occurrence(data,4)-first_occurrence(data,4)+1)
print('8. Membership:',12 in data)
print('9. Minimum:',min(data))
print('10. Maximum:',max(data))
