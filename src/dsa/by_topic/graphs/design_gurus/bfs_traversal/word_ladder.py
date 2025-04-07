"""
https://leetcode.com/problems/word-ladder/description/
"""

from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q = deque([(beginWord, 1)])
        visited = set()
        while q:
            (word, step) = q.popleft()

            if word == endWord:
                return step

            for next_word in wordList:
                if next_word not in visited and self.does_differ_by_1(word, next_word):
                    q.append((next_word, step + 1))
                    visited.add(next_word)

        return 0

    def does_differ_by_1(self, w1, w2):
        if len(w1) != len(w2):
            return False

        count = 0
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                count += 1

        return count == 1
