import sys

step = 0
l = []
inarr = []
qzsum = [0] * int(10e6+7)
mod = int(10e9+7)
for line in sys.stdin:
    if step == 0:
        a = line.split()
        k,q = int(a[0]),int(a[1])
        step += 1
        temp = 0
        for i in range(k):
            qzsum[i] = i+1
    elif q != 0:
        a = line
        t = int(a[0])
        q -= 1
        temp = 1
        for i in range(k,t):
            if i == k:
                temp = qzsum[i-1] % mod
            else:
                temp = (qzsum[i-1] - qzsum[i-k-1]) % mod
            qzsum[i] = qzsum[i-1] + temp
        print(temp%mod)    