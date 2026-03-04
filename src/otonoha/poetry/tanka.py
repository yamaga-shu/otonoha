"""Tanka poem class (5-7-5-7-7)."""

from __future__ import annotations
from otonoha.poetry.base import Poem
from otonoha.music.generator import MusicGenerator
from otonoha.music.music import Music


class Tanka(Poem):
    """A tanka poem with five phrases (5-7-5-7-7)."""

    def __init__(self) -> None:
        self._lines: list[str] = ["", "", "", "", ""]

    def line1(self, phrase: str) -> Tanka:
        self._lines[0] = phrase
        return self

    def line2(self, phrase: str) -> Tanka:
        self._lines[1] = phrase
        return self

    def line3(self, phrase: str) -> Tanka:
        self._lines[2] = phrase
        return self

    def line4(self, phrase: str) -> Tanka:
        self._lines[3] = phrase
        return self

    def line5(self, phrase: str) -> Tanka:
        self._lines[4] = phrase
        return self

    def lines(self) -> list[str]:
        return list(self._lines)

    def music(self, style: str = "ambient", **kwargs) -> Music:
        return MusicGenerator.from_poem(self, style=style, **kwargs)
