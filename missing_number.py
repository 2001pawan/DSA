# >Input: nums = [3,0,1]
# Output: 2
# Explanation: n = 3 since there are 3 numbers, 
# so all numbers are in the range [0,3]. 
# 2 is the missing number in the range since it does not appear in nums

nums=[3,0,1]

def Miss(nums):

    n=len(nums)  
    newnums=[] 

    for i in range(n+1):
        newnums.append(i)

    return set(newnums)-set(nums)

    

print(Miss(nums))


def A(nums):

    n=len(nums)
    sum_n=0
    for i in range(0,n+1):
        sum_n +=i
    # sum_n=n*(n+1)//2
    sum_nums=sum(nums)

    return sum_n - sum_nums

# print(A(nums))

