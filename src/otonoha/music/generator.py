"""Music generation logic."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from otonoha.poetry.base import Poem

from otonoha.music.music import Music
from otonoha.music.style import Style


class MusicGenerator:
    """Generates a Music object from a poem."""

    @staticmethod
    def from_poem(poem: "Poem", style: str = "lofi", **kwargs) -> Music:
        """Build a Music object from poem lines and a style name."""
        resolved_style = Style.resolve(style)
        data = {
            "lines": poem.lines(),
            "style": resolved_style,
            **kwargs,
        }
        return Music(data)
