"""General-purpose Poet class for arbitrary mora patterns."""

from __future__ import annotations
from otonoha.poetry.base import Poem
from otonoha.music.generator import MusicGenerator
from otonoha.music.music import Music


class Poet(Poem):
    """A flexible poem builder for any mora pattern.

    Pass the pattern as a concatenated integer where each digit group
    represents the mora count per phrase, e.g. ``575`` → 5-7-5.
    """

    def __init__(self, mora_pattern: int) -> None:
        self._mora_pattern = mora_pattern
        self._phrases: list[str] = []

    @property
    def mora_pattern(self) -> int:
        return self._mora_pattern

    def first(self, phrase: str) -> Poet:
        return self._set(0, phrase)

    def second(self, phrase: str) -> Poet:
        return self._set(1, phrase)

    def last(self, phrase: str) -> Poet:
        return self._set(2, phrase)

    def _set(self, index: int, phrase: str) -> Poet:
        while len(self._phrases) <= index:
            self._phrases.append("")
        self._phrases[index] = phrase
        return self

    def lines(self) -> list[str]:
        return list(self._phrases)

    def music(self, style: str = "lofi", **kwargs) -> Music:
        return MusicGenerator.from_poem(self, style=style, **kwargs)
