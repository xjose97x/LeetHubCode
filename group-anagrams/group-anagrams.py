class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        values = {}
        for s in strs:
            sorted_str = ''.join(sorted(s))
            if not sorted_str in values:
                values[sorted_str] = []
            values[sorted_str].append(s)
        return list(values.values())
