class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)  # hashmap where each key maps to a list of anagrams

        for s in strs:  # loop through each word
            count = [0] * 26  # create a list of 26 zeros, one slot for each letter a-z
            for c in s:  # loop through each character in the word
                count[ord(c) - ord('a')] += 1  # find the letter's position (a=0, b=1, c=2...) and increment its count
            res[tuple(count)].append(s)  # convert count to a tuple (so it can be a key), then group this word with others sharing the same letter counts
        return list(res.values())  # return all the groups as a list
        