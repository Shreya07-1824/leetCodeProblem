class Solution(object):
    def moveZeroes(self, nums):
        a=0
        for i in nums:
            if(i!=0):
                nums[a]=i
                a+=1

        for i in range(a,len(nums)):
            nums[i]=0
            

        