
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = defaultdict(list)
        
        for word in strs:
            wordhash = {}
            for letter in word:
                if letter in wordhash:
                    wordhash[letter] += 1
                else:
                    wordhash[letter] = 1
            
            key = tuple(sorted(wordhash.items()))
            hash[key].append(word)
            
        return list(hash.values())
