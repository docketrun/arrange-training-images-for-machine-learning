## Quickest way to random images to Structured Training Set of images dataset for Machine Learning 


Here is a tiny little python code which helps to arrange all the random images into set of arrangements order for data-set training for Machine Learning or for any use 

## Requires 


* PYTHON
* Necessary Import Modules

```python
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
	
```