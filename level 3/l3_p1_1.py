n=int(input())
fact=[1,0]
for i in range(2,n+1):
  fact.append(((i-1)*((fact[i-1]+fact[i-2])%100000007))%100000007)
print(fact[n])
