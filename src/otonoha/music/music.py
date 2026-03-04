"""Music object returned by poem.music()."""

from __future__ import annotations


class Music:
    """Represents generated music from a poem."""

    def __init__(self, data: dict) -> None:
        self._data = data

    def play(self) -> None:
        """Play the generated music (not yet implemented)."""
        raise NotImplementedError("play() is not yet implemented")

    def export(self, path: str) -> None:
        """Export the generated music to a file (not yet implemented)."""
        raise NotImplementedError("export() is not yet implemented")
