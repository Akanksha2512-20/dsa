class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = defaultdict(list)
        for i in range(len(strs)):
            s = ''.join(sorted(strs[i]))
            if s in freq:
                freq[s].append(strs[i])
            else:    
                freq[s].append(strs[i])    
        return list(freq.values())        