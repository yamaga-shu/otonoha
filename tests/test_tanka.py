from otonoha import Tanka
from otonoha.music.music import Music


def test_tanka_chaining():
    tanka = (
        Tanka()
        .line1("春過ぎて")
        .line2("夏来にけらし")
        .line3("白妙の")
        .line4("衣ほすてふ")
        .line5("天の香具山")
    )
    assert tanka.lines() == ["春過ぎて", "夏来にけらし", "白妙の", "衣ほすてふ", "天の香具山"]


def test_tanka_music_returns_music():
    music = (
        Tanka()
        .line1("春過ぎて")
        .line2("夏来にけらし")
        .line3("白妙の")
        .line4("衣ほすてふ")
        .line5("天の香具山")
        .music(style="ambient")
    )
    assert isinstance(music, Music)
