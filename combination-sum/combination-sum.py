class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def dfs(i, arr, total):
            if total == target:
                result.append(arr.copy())
                return
            if i >= len(candidates) or total > target:
                return
            
            arr.append(candidates[i])
            dfs(i, arr, total + candidates[i])
            arr.pop()
            dfs(i + 1, arr, total)
        dfs(0, [], 0)
        return result
    
