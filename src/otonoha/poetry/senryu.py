"""Senryu (and Haiku) poem class — 5-7-5 structure."""

from __future__ import annotations
from otonoha.poetry.base import Poem
from otonoha.music.generator import MusicGenerator
from otonoha.music.music import Music


class Senryu(Poem):
    """A 5-7-5 poem.

    Both senryu and haiku share this structure.
    ``Haiku`` is provided as an alias in ``otonoha.poetry.haiku``.
    """

    def __init__(self) -> None:
        self._first: str = ""
        self._second: str = ""
        self._third: str = ""

    def first(self, phrase: str) -> Senryu:
        self._first = phrase
        return self

    def second(self, phrase: str) -> Senryu:
        self._second = phrase
        return self

    def third(self, phrase: str) -> Senryu:
        self._third = phrase
        return self

    def lines(self) -> list[str]:
        return [self._first, self._second, self._third]

    def music(self, style: str = "jazz", **kwargs) -> Music:
        return MusicGenerator.from_poem(self, style=style, **kwargs)
