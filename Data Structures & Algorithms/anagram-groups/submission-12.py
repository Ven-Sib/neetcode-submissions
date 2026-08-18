class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = defaultdict(list)

        for i in strs:
            x = ''.join(sorted(i))
            
            dict1[x].append(i)

        return list(dict1.values())

  