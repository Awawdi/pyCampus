import winsound

freqs = {"la": 220,
         "si": 247,
         "do": 261,
         "re": 293,
         "mi": 329,
         "fa": 349,
         "sol": 392,
         }

notes = "sol,250-mi,250-mi,500-fa,250-re,250-re,500-do,250-re,250-mi,250-fa,250-sol,250-sol,250-sol,500"

one_note = notes.split("-")
for note in one_note:
    mid = note.split(",")
    winsound.Beep(freqs[mid[0]], int(mid[1]))
    winsound.Beep(261, 10000)
    winsound.Beep(349, 100)
    winsound.Beep(392, 500)
    winsound.Beep(261, 250)
    winsound.Beep(255,267)
    winsound.Beep(100, 77)
    winsound.Beep(88, 40)
    winsound.Beep(145, 54)
    winsound.Beep(100, 250)
