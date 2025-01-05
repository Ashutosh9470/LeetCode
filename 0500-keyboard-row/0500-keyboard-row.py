class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        
        a = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
        b =  ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
        c = ['z', 'x', 'c', 'v', 'b', 'n', 'm']
        sol = []
        for i in words:
            x = True
            y = True
            z = True
            for j in i.lower():
                if j not in a:
                    x = False
                if j not in b:
                    y = False
                if j not in c:
                    z = False

            if x or y or z:
                sol.append(i)
        return sol