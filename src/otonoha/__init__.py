"""
otonoha — Turn Japanese poetry into music.

Usage:
    from otonoha import Haiku, Tanka, Senryu, Poet
"""

from otonoha.poetry.haiku import Haiku
from otonoha.poetry.tanka import Tanka
from otonoha.poetry.senryu import Senryu
from otonoha.poetry.poet import Poet

__all__ = ["Haiku", "Tanka", "Senryu", "Poet"]
