import copy
import random
from pythonmagickwand.image import Image
from pythonmagickwand.wand import LANCZOS_FILTER, TRANSPARENT_COLORSPACE
from pythonmagickwand.color import Color, BLACK, YELLOW, TRANSPARENT

YELLOW = Color('#ffcc33')
m = Image('monkey.png')
m.opaque_paint(BLACK, YELLOW, 10)
m.scale((500,500))
m.compression_quality = 95

im = Image()
im.colorspace = TRANSPARENT_COLORSPACE
im.size = (4000, 800)
im.format = 'PNG'
im.background_color = TRANSPARENT
_w, _h = im.size

num = range(3000)
for i in num:
    ratio = (i+1.)/len(num)

    random.seed()
    _min = int(100*ratio+100)
    w = random.randint(_min, max(int(400*ratio), _min))

    c = copy.copy(m)
    c.scale((w, w))
    c.rotate(random.randint(0, 360), TRANSPARENT)
    c.modulate(brightness=i*25/len(num) + 75)

    a, b = 0.5*_h - _h/(10*ratio+3), _h/5
    y = abs(min(random.gauss(a, b), _h))
    im.composite(c, (random.randint(0-c.size[0], _w), y))

im.scale((1000, 200))
im.quantize(32, TRANSPARENT_COLORSPACE)
#im.opaque_paint(YELLOW, YELLOW, 10)
im.save('out.png')
