class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = {}
        for i in strs:
            x = "".join(sorted(i))
            if x not in dict1:
                dict1[x] = [i]
            else:
                dict1[x].append(i)
        return list(dict1.values())

       