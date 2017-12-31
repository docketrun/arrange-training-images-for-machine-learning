from PIL import Image
import glob, os
import itertools
counter = itertools.count()

size = 500, 300

for infile in glob.glob("*.jpg"):
    file, ext = os.path.splitext(infile)
    im = Image.open(infile)
    im.thumbnail(size)
    im.save("image" + str(next(counter)) +".jpg", "JPEG")
	