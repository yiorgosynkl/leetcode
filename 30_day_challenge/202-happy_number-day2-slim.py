class Solution:
    def isHappy(self, n: int) -> bool:
        x = set([]) # existance set
        m = {'0':0,'1':1,'2':4,'3':9,'4':16,'5':25,'6':36,'7':49,'8':64,'9':81}
        while n != 1:
            n = sum([m[c] for c in str(n)])
            if n in x: return False
            x.add(n)
        return True