from otonoha import Haiku, Senryu
from otonoha.music.music import Music


def test_haiku_is_senryu_alias():
    assert Haiku is Senryu


def test_haiku_chaining():
    haiku = (
        Haiku()
        .first("古池や")
        .second("蛙とびこむ")
        .third("水の音")
    )
    assert haiku.lines() == ["古池や", "蛙とびこむ", "水の音"]


def test_haiku_music_returns_music():
    music = (
        Haiku()
        .first("古池や")
        .second("蛙とびこむ")
        .third("水の音")
        .music(style="jazz")
    )
    assert isinstance(music, Music)
