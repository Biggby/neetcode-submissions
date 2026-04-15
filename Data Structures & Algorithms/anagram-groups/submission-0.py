class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groupped = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord ('a')] += 1
            groupped[tuple(count)].append(word)

        return list(groupped.values()) 
