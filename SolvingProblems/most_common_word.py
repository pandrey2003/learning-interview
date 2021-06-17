import string
from collections import Counter


class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        paragraph = paragraph.translate(str.maketrans(string.punctuation, ' ' * len(string.punctuation))).lower()
        not_banned_words_in_para = [word for word in paragraph.split() if word not in banned]
        word_counts = Counter(not_banned_words_in_para)
        return word_counts.most_common(1)[0][0]
