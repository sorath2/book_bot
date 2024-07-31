import os
import sys

BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    punctuation_marks = ',.!?:;'
    max_text = text[start:start + size]
    res_text = ''
    if len(text) > start + size and text[start + size] in punctuation_marks:
        symbol = text[start + size]
        while symbol in punctuation_marks:
            symbol = max_text[-1]
            max_text = max_text[:-1]

    for index, letter in enumerate(max_text[::-1]):
        if letter in punctuation_marks:
            res_text = max_text[:len(max_text) - index]
            return res_text, len(res_text)


def prepare_book(path: str) -> None:
    pass


prepare_book(os.path.join(sys.path[0], os.path.normpath(BOOK_PATH)))
