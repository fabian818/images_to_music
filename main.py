# library imports
import math
import abjad
from PIL import Image, ImageFilter

# own library imports
import music
import pitch
SCALE_PITCH = 30
SCALE_TIME = 0.5
SCALE_VOLUME = 0.2
MINOR = 17

size = 20, 20
im = Image.open( 'gary.jpeg' )
im = im.convert('RGB')
im.thumbnail(size)
values = [[e[0], e[1], e[2]] for e in list(im.getdata())]
notes = [
    [int(v[0] / max(values)[0] * SCALE_PITCH),
    round((v[1] / max(values)[1]) * SCALE_TIME, 2),
    round((v[2] / max(values)[2]) * SCALE_VOLUME, 2)] for v in values]
print(notes)

for note in notes:
    note[2] += .09
    f = music.create_pulse_function(pitch.inverse(note[0], MINOR), note[2])
    if note[1] > 0.45:
        note[1] = 0.5
    elif note[1] > 0.3:
        note[1] = 0.25 
    else:
        note[1] = 0.125
    print(note)
    music.generate(pulse_function=f, duration=note[1])