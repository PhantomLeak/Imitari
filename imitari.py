# This is imitari, the code I wrote but was inevitably removed from for no reason at all...fun

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

image.thumbnail(size, Image.ANTIALIAS)

image.save('test.jpg')


