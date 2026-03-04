"""Haiku is an alias for Senryu — both use a 5-7-5 structure."""

from otonoha.poetry.senryu import Senryu

# Haiku and Senryu share the same 5-7-5 form.
# Kigo (seasonal word) detection is out of scope for initial development.
Haiku = Senryu

__all__ = ["Haiku"]
