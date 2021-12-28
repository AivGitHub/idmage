import magic
from pathlib import Path

from image.image import Image

mime = magic.Magic(mime=True)


class Maintain(object):

    def __init__(self, **kwargs):
        _path = Path(kwargs.get('path')[0])
        _path_absolute = _path.absolute()

        self.path = str(_path_absolute)
        self.delete_exif = kwargs.get('delete_exif')
        self.quiet = kwargs.get('quiet')
        self.recursive = kwargs.get('recursive')

        self.is_dir = Path.is_dir(_path_absolute)

    def __str__(self):
        return str(self.path)

    def process(self):
        if self.is_dir:
            pass
        else:
            im = Image(self.path)

            im_no_exif = im.get_no_exif()
            im_no_exif.save(f'{im.dir_name}/{im.basename}_no_exif{im.extension}')

            del im
            del im_no_exif

            if self.delete_exif:
                path_to_delete = Path(self.path)
                path_to_delete.unlink()
