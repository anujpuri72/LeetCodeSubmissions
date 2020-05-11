from collections import defaultdict
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        resa=defaultdict(lambda:-1) 
        for keys in S: 
            resa[keys] = resa.get(keys, 0) + 1
        count=0
        for i in J:
            if resa[i]!=-1:
                count+=resa[i]
        return count