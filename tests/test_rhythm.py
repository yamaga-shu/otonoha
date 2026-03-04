from otonoha.utils.syllable import count_mora
from otonoha.rhythm.analyzer import RhythmAnalyzer


def test_count_mora_5():
    # ふるいけや = 5 mora (hiragana only for deterministic counting)
    assert count_mora("ふるいけや") == 5


def test_count_mora_7():
    # かわずとびこむ = 7 mora
    assert count_mora("かわずとびこむ") == 7


def test_count_mora_small_kana_not_counted():
    # っ and ゃ are small kana and should not be counted as separate mora
    assert count_mora("びょういん") == 4  # byo-u-i-n → びょ=1, う=1, い=1, ん=1


def test_rhythm_analyzer_haiku():
    analyzer = RhythmAnalyzer()
    # Use hiragana readings: ふるいけや / かわずとびこむ / みずのおと
    result = analyzer.analyze(["ふるいけや", "かわずとびこむ", "みずのおと"])
    assert result == [5, 7, 5]
