class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        resa = defaultdict(lambda: -1)
        for keys in ransomNote:
            resa[keys] = resa.get(keys, 0) + 1
        resb = defaultdict(lambda: -1)
        for keys in magazine:
            resb[keys] = resb.get(keys, 0) + 1
        for a, b in resa.items():
            if(resb[a] == -1 or resa[a] > resb[a]):
                return False
        return True
