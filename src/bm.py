from typing import Dict


def make_km_table(pattern: str) -> Dict[str, int]:
    table = dict()
    for index, char in reversed(list(enumerate(pattern))):
        table[char] = index
    return table


class Bm(object):
    def __init__(self, text: str, pattern: str):
        self.text = text
        self.pattern = pattern
        self.table = make_km_table(pattern)
        self.pattern_length = len(pattern)
        self.text_length = len(text)

    def decide_slide_width(self, pat_index: int, char: str) -> int:
        assert len(char) == 1
        slide_width = pat_index - self.table.get(char, -1)
        return max(1, slide_width)

    def _calculate_text_pattern_difference(self) -> int:
        return (self.text_length - self.pattern_length + 1)

    def _get_index_of_the_first_text_pattern_mismatch(self, slide: int) -> int:

        for index, pat_char in reversed(list(enumerate(self.pattern))):
            text_char = self.text[index + slide]
            matched = pat_char == text_char
            if not matched:
                return index
        else:
            return -1

    def search(self) -> int:
        index_after_slide = 0
        text_pat_diff = self._calculate_text_pattern_difference()
        while index_after_slide < text_pat_diff:
            pat_index = self._get_index_of_the_first_text_pattern_mismatch(
                index_after_slide)

            pattern_match_found = pat_index < 0

            if pattern_match_found:
                return index_after_slide
            else:
                index_after_slide += self.decide_slide_width(
                    pat_index,
                    self.text[index_after_slide + pat_index],
                )
        return -1
