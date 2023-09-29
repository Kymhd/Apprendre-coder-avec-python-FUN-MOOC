x = float(input())
t, n, s = 1, 0, 0
f=(1, 1)
while abs(t) > 1e-6:
    t = (-1)**n * x**(2*n+1) / f[1]
    s += t
    n += 1
    f=(f[0] + 2, f[1] * (f[0] + 1) * (f[0] + 2))
print(s)