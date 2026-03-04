"""Base class for all poem types."""

from __future__ import annotations
from abc import ABC, abstractmethod
from otonoha.music.music import Music


class Poem(ABC):
    """Abstract base class for Japanese poem types."""

    @abstractmethod
    def music(self, style: str = "lofi", **kwargs) -> Music:
        """Generate a Music object from this poem."""
        ...
