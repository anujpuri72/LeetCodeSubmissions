class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        a = []
        if(len(num) == k):
            return "0"
        for i in num:
            a.append(i)
        count = 0
        while(count < k):
            incount = count
            for i in range(len(a)-1):
                if (a[i] > a[i+1]):
                    a.pop(i)
                    count += 1
                    break

            if(incount == count and a[i+1] == a[-1]):
                a.pop(i+1)
                count += 1

        return str(int("".join(a)))
