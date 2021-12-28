import mimetypes
from pathlib import Path

from PIL import Image as pil_image
import magic

mime = magic.Magic(mime=True)


class Image(object):

    def __init__(self, path, **kwargs):
        _path = Path(path)
        _path_absolute = _path.absolute()

        self.is_dir = Path.is_dir(_path_absolute)
        self.path = str(_path_absolute)
        self.mime_type = self.get_mime_type()
        self.extension = mimetypes.guess_extension(self.mime_type)
        self.basename = _path.resolve().stem
        self.dir_name = str(_path_absolute.parent.resolve())

    def __str__(self):
        return self.path

    def get_no_exif(self):
        image = pil_image.open(self.path)

        data = list(image.getdata())
        image_without_exif = pil_image.new(image.mode, image.size)
        image_without_exif.putdata(data)

        return image_without_exif

    def get_mime_type(self):
        if self.is_dir:
            return 'inode/directory'
        else:
            return mime.from_file(self.path)
