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

    def decide_slide_width(self, c: str) -> int:
        assert len(c) == 1
        return self.table.get(c, -1)

    def search(self) -> int:
        current_index = len(self.pattern) - 1
        slide_width = 0
        while slide_width < (len(self.text) - len(self.pattern) + 1):
            current_index = len(self.pattern) - 1

            while current_index >= 0 and self.pattern[
                    current_index] == self.text[slide_width + current_index]:
                current_index -= 1

            if current_index < 0:
                return slide_width
            else:
                slide_width += max(1, current_index - self.decide_slide_width(
                    self.text[slide_width + current_index]))
        return -1
