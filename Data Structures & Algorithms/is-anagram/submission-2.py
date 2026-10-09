class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        smap = dict()
        tmap = dict()

        for ss, ts in zip(s, t):
            if ss not in smap:
                smap[ss] = 1

            if ts not in tmap:
                tmap[ts] = 1

            smap[ss] += 1
            tmap[ts] += 1
        
        for ss, sc in smap.items():
            tc = tmap.get(ss, None)
            if sc != tc:
                return False
        
        return True
        
