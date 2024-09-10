class Solution(object):

    nums = [-1,0,1,2,-1,-4]

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        triplets = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if (i != j and j != k and i != k) and (nums[i] + nums[j]) == nums[k]:
                        triplet = []
                        triplet.append(nums[i])
                        triplet.append(nums[j])
                        triplet.append(nums[k])
                        triplets.append(triplets)
        #return triplets 
    
        print(triplets)