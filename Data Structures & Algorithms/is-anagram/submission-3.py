class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            des = []
            for st in s:
                if s.count(st) != t.count(st):
                    return False
                if st not in des:
                    des.append(st)
            for st1 in t:
                if st1 not in des:
                    return False
            return True
        
        