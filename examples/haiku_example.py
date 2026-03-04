"""Basic usage examples from the README."""
from otonoha import Haiku, Senryu, Poet

# --- Haiku example ---
haiku = (
    Haiku()
      .first("古池や")
      .second("蛙とびこむ")
      .third("水の音")
)

music = haiku.music(style="lofi", tempo=80)
# music.play()       # not yet implemented
# music.export("frog_song.mp3")  # not yet implemented

# --- Senryu example ---
senryu_music = (
    Senryu()
      .first("会議中")
      .second("ミュート忘れて")
      .third("猫鳴いた")
      .music(style="jazz")
)

# --- General Poet example ---
poet_music = (
    Poet(575)
      .first("古池や")
      .second("蛙とびこむ")
      .last("水の音")
      .music(
          style="lofi",
          instrument=["piano", "shakuhachi"],
          tempo=70,
      )
)
