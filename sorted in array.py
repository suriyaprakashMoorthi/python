limit=int(input())
l1=list(map(int,input().split()))[:limit]
l1.sort()
print(*l1, sep = ' ')

