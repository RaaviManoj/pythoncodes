def permu(nums,n,c):
    if c==n:
        print(nums)
        #return
    else:
        for i in range(c,n+1):
            nums[i],nums[c]=nums[c],nums[i]
            permu(nums,n,c+1)
            nums[i],nums[c]=nums[c],nums[i]

permu([1,2,3],2,0)
