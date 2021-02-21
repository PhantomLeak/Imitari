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

'''
def convert_heic_jpg(fp):

        heif_file = pyheif.read(open(fp).read())
        image = Image.frombytes(
            heif_file.mode, 
            heif_file.size, 
            heif_file.data,
            "raw",
            heif_file.mode,
            heif_file.stride,
        )
        buf = io.BytesIO()
        image.save(buf, format="JPEG")
        buf.seek(0)
        return buf.getvalue()


    def resize(fp, size):
        image = Image.open(fp)
        image.thumbnail(size, Image.ANTIALIAS)
        buf = io.BytesIO()
        image.save(buf)
        buf.seek(0)
        return buf.getvalue()
'''
