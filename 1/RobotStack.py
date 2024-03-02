import sys

def recurrence(idx_n,idx_b,k,dp):
    # Base Condition
    if idx_n==0:
        if idx_b!=0:
            return 0
        else:
            return 1
    # If sub problem is previously solved tehn return it.
    if dp[idx_n][idx_b] !=-1:
        return dp[idx_n][idx_b]
    res=0
    for j in range(min(idx_b+1,k+1)):
        res=res+recurrence(idx_n-1,idx_b-j,k,dp)
    dp[idx_n][idx_b]=res
    return res

def iterative(n,b,k):
    #initialize dp array with 0 value
    dp = [[0] * (b + 1) for _ in range(n + 1)]
    #base case
    dp[0][0]=1
    #loop through stacks
    for i in range(1,n+1):
        #loop through robots
        for j in range(0,b+1):
            #loop through number of robots to put in current stack i
            for idx_k in range(min(j+1,k+1)):
                #number of ways in current state i is sum of number of ways of previous states 
                # with all different remaining number of robots(j-idx_k)
                dp[i][j]=dp[i][j]+dp[i-1][j-idx_k]
    return dp[n][b]


if __name__ == '__main__':
   
    with open(sys.argv[1], 'r') as my_file:
        Lines = my_file.readlines()
        for line in Lines:
            b,n,k=line.strip().split(',') 
            b=int(b)
            n=int(n)   
            k=int(k)
            
            dp = [[-1] * (b + 1) for _ in range(n + 1)]
            number_of_ways_recursive=recurrence(n,b,k,dp)
            print("("+str(b)+","+str(n)+","+str(k)+") = "+str(number_of_ways_recursive))
            #number_of_ways_iterative=iterative(n,b,k)
            #print('number of ways using iterative approach  is : ',number_of_ways_iterative)