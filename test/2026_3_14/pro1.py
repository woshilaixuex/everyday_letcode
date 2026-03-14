import sys 
def check(num) -> int:
    ans = 0
    for i in range(1,num+1):
        if num % i == 0:
            ans += 1
    return ans
for line in sys.stdin:
    a = line.split()
    l,r = int(a[0]),int(a[1])
    ans = 0
    for i in range(l,r+1):
        if check(i) % 2 != 0:
            ans += 1
    print(ans)