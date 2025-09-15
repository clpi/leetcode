#
# @lc app=leetcode id=30 lang=python3
#
# [30] Substring with Concatenation of All Words
#

# @lc code=start
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_length = len(words[0])
        total_words_length = word_length * len(words)
        word_count = Counter(words)
        result_indices = []

        for i in range(len(s) - total_words_length + 1):
            seen_words = defaultdict(int)
            j = 0

            while j < total_words_length:
                word_start = i + j
                word_end = word_start + word_length
                word = s[word_start:word_end]

                if word in word_count:
                    seen_words[word] += 1
                    if seen_words[word] > word_count[word]:
                        break
                else:
                    break

                j += word_length

            if j == total_words_length:
                result_indices.append(i)

        return result_indices
        
# @lc code=end

