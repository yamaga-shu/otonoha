"""Haiku poem class (5-7-5)."""

from __future__ import annotations
from otonoha.poetry.base import Poem
from otonoha.music.generator import MusicGenerator
from otonoha.music.music import Music


class Haiku(Poem):
    """A haiku poem with three phrases (5-7-5)."""

    def __init__(self) -> None:
        self._first: str = ""
        self._second: str = ""
        self._third: str = ""

    def first(self, phrase: str) -> Haiku:
        self._first = phrase
        return self

    def second(self, phrase: str) -> Haiku:
        self._second = phrase
        return self

    def third(self, phrase: str) -> Haiku:
        self._third = phrase
        return self

    def lines(self) -> list[str]:
        return [self._first, self._second, self._third]

    def music(self, style: str = "lofi", **kwargs) -> Music:
        return MusicGenerator.from_poem(self, style=style, **kwargs)
