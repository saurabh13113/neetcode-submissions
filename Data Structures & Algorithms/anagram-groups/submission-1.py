class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dc = {}
        for st in strs:
            sts = "".join(sorted(st))
            if sts not in dc:
                dc[sts] = [st]
            else:
                dc[sts].append(st)
        ret =[]
        for k in dc:
            ret.append(dc[k])
        return ret