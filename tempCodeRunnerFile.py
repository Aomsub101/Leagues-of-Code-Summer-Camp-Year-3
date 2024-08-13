s = list(map(int, input().split()))

num = 0
for i in range(len(s)):
    num += s[i] * (10**(len(s)-i-1))

num+=1

# print("[", end = '')
cnt = len(str(num))
for i in range(cnt):
    tmp = num//(10**(cnt-i-1))
    num -= tmp*(10**(cnt-i-1))
    print(tmp, end= '')
    if i != cnt-1:
        print(' ', end='')
# print("]", end = '')    

