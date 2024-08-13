n = int(input())

l = list(map(int, input().split()))

check = []
cnt = 0
for i in range (n):
    if l[i] not in check:
        check.append(l[i])
        cnt+=1

print(cnt+1)