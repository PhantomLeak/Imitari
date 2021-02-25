

import pyheif
from PIL import Image
import io

file = pyheif.read(open('sample.heic', 'rb').read())

image = Image.frombytes(
	file.mode,
	file.size,
	file.data,
	"raw",
	file.mode,
	file.stride,
	)

buf = io.BytesIO()

image.save(buf, format="JPEG")

image = Image.open(buf)

size = (100,100)

image.thumbnail(size, Image.ANTIALIAS)

image.save('test.jpg')


