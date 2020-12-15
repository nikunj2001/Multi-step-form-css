for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    l2=[]
    for i in range(1,n):
        ele=l[i]
        l2.insert(l[i-1],i)
    print(*l2)