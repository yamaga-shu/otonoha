# otonoha

**otonoha** is an experimental library that turns Japanese poetry into music.

Write a poem such as a **haiku**, **tanka**, or **senryu**, and generate music from its rhythm, mood, and structure using AI.

The name *otonoha* comes from the Japanese phrase **言の葉 (kotonoha)** — "words as leaves".
In this project, words grow into **sound**.

🌿 Words → Sound → Music

---

## Concept

Japanese poetry has a strong rhythmic structure:

- **Haiku**: 5-7-5
- **Tanka**: 5-7-5-7-7
- **Senryu**: 5-7-5

These rhythms naturally resemble musical phrasing.

`otonoha` explores the idea that **poetry structure can become musical structure**.

A poem becomes:

- melody
- rhythm
- harmony
- mood

---

## Installation (future)

```bash
pip install otonoha
```

## Basic Example

Generate music from a haiku.

```python
from otonoha import Haiku

haiku = (
    Haiku()
      .first("古池や")
      .second("蛙とびこむ")
      .third("水の音")
)

music = haiku.music(
    style="lofi",
    tempo=80
)

music.play()
```

## Another Example

```python
from otonoha import Haiku

music = (
    Haiku()
      .first("古池や")
      .second("蛙とびこむ")
      .third("水の音")
      .music(style="J-POP")
)

music.export("frog_song.mp3")
```

## Tanka Example

Future support for tanka (5-7-5-7-7).

```python
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
```

## Senryu Example

```python
from otonoha import Senryu

music = (
    Senryu()
      .first("会議中")
      .second("ミュート忘れて")
      .third("猫鳴いた")
      .music(style="jazz")
)
```

## Future Features

- 🎵 Haiku → music generation

- 🎵 Tanka → melody structure

- 🎵 Senryu → rhythm generation

- 🎵 Style selection

- 🎵 MIDI export

- 🎵 AI melody generation

- 🎵 Japanese instrument presets (shamisen / koto / shakuhachi)

## Example API Vision

```python
from otonoha import Poet

p = Poet(575)

music = (
    p.first("古池や")
     .second("蛙とびこむ")
     .last("水の音")
     .music(
         style="lofi",
         instrument=["piano", "shakuhachi"],
         tempo=70
     )
)
```

## Philosophy

Poetry is already music.

Japanese poetry has rhythm, silence, and space.

otonoha tries to translate that beauty into sound.

## Status

🚧 Experimental idea / research project

## License

MIT
