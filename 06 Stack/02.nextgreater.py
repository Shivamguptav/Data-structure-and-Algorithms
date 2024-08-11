#grneral solution


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[-1]*len(nums1)
        d={n:i for i,n in enumerate(nums1)}
        for i in range(len(nums2)):
            if nums2[i] not in d:
                continue
            for j in range(i+1,len(nums2)):
                if nums2[i]<nums2[j]:
                    idx = d[nums2[i]]
                    res[idx]=nums2[j]
                    break
        return res
    


# optimize solution using stack


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d={n:i for i,n in enumerate(nums1)}
        res=[-1]*len(nums1)
        stack = []
        for i in range(len(nums2)):
            cur= nums2[i]
            while stack and cur > stack[-1]:
                val=stack.pop()
                idx = d[val]
                res[idx] = cur
            if cur in d:
                stack.append(cur)
        return res

