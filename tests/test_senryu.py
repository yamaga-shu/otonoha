from otonoha import Senryu
from otonoha.music.music import Music


def test_senryu_chaining():
    senryu = (
        Senryu()
        .first("会議中")
        .second("ミュート忘れて")
        .third("猫鳴いた")
    )
    assert senryu.lines() == ["会議中", "ミュート忘れて", "猫鳴いた"]


def test_senryu_music_returns_music():
    music = (
        Senryu()
        .first("会議中")
        .second("ミュート忘れて")
        .third("猫鳴いた")
        .music(style="jazz")
    )
    assert isinstance(music, Music)
