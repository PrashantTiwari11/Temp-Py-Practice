# 65_sorting_algorithms.py
# Sorting Algorithms - 10 practical programs/features

def bubble_sort(a):
    a=a[:]
    for i in range(len(a)):
        for j in range(len(a)-1-i):
            if a[j]>a[j+1]: a[j],a[j+1]=a[j+1],a[j]
    return a

def selection_sort(a):
    a=a[:]
    for i in range(len(a)):
        k=min(range(i,len(a)),key=a.__getitem__); a[i],a[k]=a[k],a[i]
    return a

def insertion_sort(a):
    a=a[:]
    for i in range(1,len(a)):
        key,j=a[i],i-1
        while j>=0 and a[j]>key: a[j+1]=a[j]; j-=1
        a[j+1]=key
    return a

def merge_sort(a):
    if len(a)<=1:return a[:]
    m=len(a)//2; left,right=merge_sort(a[:m]),merge_sort(a[m:]); out=[]
    while left and right: out.append(left.pop(0) if left[0]<=right[0] else right.pop(0))
    return out+left+right

def quick_sort(a):
    if len(a)<=1:return a[:]
    p=a[len(a)//2]
    return quick_sort([x for x in a if x<p])+[p]*a.count(p)+quick_sort([x for x in a if x>p])

data=[64,25,12,22,11]
print('1. Original:',data)
print('2. Bubble:',bubble_sort(data))
print('3. Selection:',selection_sort(data))
print('4. Insertion:',insertion_sort(data))
print('5. Merge:',merge_sort(data))
print('6. Quick:',quick_sort(data))
print('7. Built-in:',sorted(data))
print('8. Descending:',sorted(data,reverse=True))
print('9. Strings:',sorted(['banana','apple','cherry']))
print('10. Key sorting:',sorted(['ccc','a','bb'],key=len))
