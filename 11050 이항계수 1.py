n, k = map(int,input().split())
n_fac = 1
k_fac = 1
nk_fac = 1
for i in range(1,n+1):
    n_fac *= i
for j in range(1,k+1):
    k_fac *= j
for k in range(1,n-k+1):
    nk_fac *= k
print(n_fac//(k_fac*nk_fac))