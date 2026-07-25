class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ns = ""
        maxlen = 0
        for ch in s:
            if ch in ns:
                idx = ns.index(ch)
                ns = ns[idx+1:]
            ns += ch
            maxlen = max(maxlen, len(ns))
        return maxlen