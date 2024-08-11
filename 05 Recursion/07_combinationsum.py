class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        ds=[]
        Combinations(0,target,candidates,ans,ds)
        return ans
def Combinations(index,target,candidates,ans,ds):
    if index == len(candidates):
        if target == 0:
            ans.append(ds[:])
        return 
    if candidates[index]<= target:
        ds.append(candidates[index])
        Combinations(index, target-candidates[index] , candidates, ans, ds)
        ds.pop()
    Combinations(index+1, target, candidates,ans , ds)

# 2nd solution

from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        ds = []
        self.findCombination(0, target, candidates, ans, ds)
        return ans
    
def findCombination(self, ind: int, target: int, arr: List[int], ans: List[List[int]], ds: List[int]) -> None:
        if ind == len(arr):
            if target == 0:
                ans.append(ds[:])
            return
        if arr[ind] <= target:
            ds.append(arr[ind])
            self.findCombination(ind, target - arr[ind], arr, ans, ds)
            ds.pop()
        self.findCombination(ind + 1, target, arr, ans, ds)
