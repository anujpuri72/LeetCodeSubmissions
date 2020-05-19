class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if(len(s)<len(p)):
            return 
        i=len(p)
        count=[]
        check={}
        tocheck={}
        for j in range(len(p)):
            check[p[j]]=check.get(p[j],0)+1
            tocheck[s[j]]=tocheck.get(s[j],0)+1
        if(check==tocheck):
            count.append(0)
        while (i< len(s)):
            tocheck[s[i]]=tocheck.get(s[i],0)+1  
            tocheck[s[i-len(p)]]=tocheck[s[i-len(p)]] -1
            if(tocheck[s[i-len(p)]]==0):
                del tocheck[s[i-len(p)]]
            if(check==tocheck):
                count.append(i-len(p)+1)
            i+=1
        return count      
            
            
            
            