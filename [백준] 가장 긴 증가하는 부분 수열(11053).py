N=int(input())
numbers = [0]+list(map(int,input().split()))
dp = [0]+[1]*N
for i in range(1,N+1):
    for j in range(i):
        if numbers[i] > numbers[j] :
            dp[i] = max(dp[i],dp[j]+1)
print(max(dp))
