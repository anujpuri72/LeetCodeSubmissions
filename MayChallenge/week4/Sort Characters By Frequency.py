class Solution:
    def frequencySort(self, s: str) -> str:
        char = {}
        for i in s:
            char[i] = char.get(i, 0)+1
        a = sorted(char.items(), key=lambda x: x[1], reverse=True)

        l = []
        for i in a:
            l.append(i[0]*i[1])
        return "".join(l)
