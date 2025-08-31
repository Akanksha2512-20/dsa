class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = len(s1)
        l =0
        mp_s1 = Counter(s1)
        mp_s2 = {}
        for r in range(len(s2)):
            mp_s2[s2[r]] = mp_s2.get(s2[r],0)+1
            if r-l+1 > len(s1):
                mp_s2[s2[l]]-=1
                if mp_s2[s2[l]] == 0:   
                    del mp_s2[s2[l]]
                l+=1
            if mp_s2==mp_s1:
                return True
        return False

        