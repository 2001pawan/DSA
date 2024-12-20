#given a target,find the 2 elements that will add up to target

arr=[1, 2, 4, 6, 9, 10]


def find(target):

    i=0
    j=0
    # found=False

    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j]==target:
                # found=True
                # print(i,j)
                return (i,j)
    
    print("aa")
    # if found == False:
    #     print("-1")

    return -1
    

a=find(5)
print(a)