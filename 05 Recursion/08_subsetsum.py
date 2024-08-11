from typing import List
class Solution:
    def subsetSums(self, arr: List[int], n: int) -> List[int]:
        ans = []


        def subsetSumsHelper(ind, sum):
            if ind == n:
                ans.append(sum)
                return
            # element is picked
            subsetSumsHelper(ind + 1, sum + arr[ind])
            # element is not picked
            subsetSumsHelper(ind + 1, sum)
        subsetSumsHelper(0, 0)
        ans.sort()
        return ans




if __name__ == "__main__":
    arr = [3, 1, 2]
    ans = Solution().subsetSums(arr, len(arr))
    print("The sum of each subset is")
    for sum in ans:
        print(sum, end=" ")
    print()