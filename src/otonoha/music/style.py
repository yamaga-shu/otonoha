"""Style definitions for music generation."""

from __future__ import annotations

_KNOWN_STYLES = {
    "lofi",
    "ambient",
    "jazz",
    "J-POP",
    "classical",
}


class Style:
    """Validates and resolves music style names."""

    @staticmethod
    def resolve(name: str) -> str:
        if name not in _KNOWN_STYLES:
            raise ValueError(
                f"Unknown style '{name}'. "
                f"Choose from: {sorted(_KNOWN_STYLES)}"
            )
        return name
