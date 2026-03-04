"""Rhythm analysis for Japanese poems."""

from __future__ import annotations
from otonoha.utils.syllable import count_mora


class RhythmAnalyzer:
    """Analyzes the rhythmic structure of a poem."""

    def analyze(self, lines: list[str]) -> list[int]:
        """Return mora counts for each line."""
        return [count_mora(line) for line in lines]
