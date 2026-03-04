"""Tanka usage example from the README."""
from otonoha import Tanka

music = (
    Tanka()
      .line1("春過ぎて")
      .line2("夏来にけらし")
      .line3("白妙の")
      .line4("衣ほすてふ")
      .line5("天の香具山")
      .music(style="ambient")
)
# music.play()
