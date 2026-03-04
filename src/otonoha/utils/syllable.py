"""Japanese mora (syllable) counting utilities."""

from __future__ import annotations

# Unicode ranges for Japanese kana
_HIRAGANA = range(0x3041, 0x3097)
_KATAKANA = range(0x30A1, 0x30F7)
# CJK Unified Ideographs (kanji)
_KANJI = range(0x4E00, 0x9FFF + 1)

# Small kana that attach to the preceding mora (not counted separately)
_SMALL_KANA = set("ぁぃぅぇぉっゃゅょゎァィゥェォッャュョヮ")


def count_mora(text: str) -> int:
    """Count the number of mora in a Japanese text string.

    Kana characters are counted directly.
    Kanji are counted as 1 mora each (stub — accurate counting
    requires kana conversion, e.g. via pykakasi).
    """
    count = 0
    for ch in text:
        if ch in _SMALL_KANA:
            continue
        cp = ord(ch)
        if cp in _HIRAGANA or cp in _KATAKANA or cp in _KANJI:
            count += 1
    return count
