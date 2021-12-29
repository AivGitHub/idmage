import magic
from pathlib import Path
import sys

from image.image import Image
from idmage import IDmageUtils

mime = magic.Magic(mime=True)


class Maintain(object):

    def __init__(self, **kwargs) -> None:
        _path_arg = kwargs.get('path')

        assert _path_arg != [], 'Path is required argument'

        _path = Path(_path_arg[0])
        _path_absolute = _path.absolute()

        self.path = str(_path_absolute)
        self.delete_exif = kwargs.get('delete_exif')
        self.quiet = kwargs.get('quiet')
        self.recursive = kwargs.get('recursive')
        self.message = kwargs.get('message')
        self.steganography = kwargs.get('steganography')

        self.is_dir = Path.is_dir(_path_absolute)

    def __str__(self) -> str:
        return str(self.path)

    def process(self) -> None:

        self.stdout('Started process..')

        if self.is_dir:
            # TODO: recursive process
            pass
        else:
            img = Image(self.path)

            self.stdout('Getting no exif file')

            im_no_exif = img.get_no_exif()

            self.secure_save(img, im_no_exif)
            self.delete_by_path(img.path)

            del img
            del im_no_exif

    def secure_save(self, img, new_img):

        while True:
            random_string = IDmageUtils.get_random_string(quantity=4)
            new_file_name = f'{img.dir_name}/{img.basename}_no_exif_{random_string}{img.extension}'
            p = Path(new_file_name)

            if not p.exists():
                self.stdout(f'Saving no exif file: {new_file_name}')
                new_img.save(new_file_name)
                return

    def delete_by_path(self, path) -> None:
        if self.delete_exif:
            self.stdout(f'Deleting file {path}')
            path_to_delete = Path(path)
            path_to_delete.unlink()

    def stdout(self, message, out_type='stdout') -> None:

        if self.quiet:
            return

        if out_type == 'stdout':
            sys.stdout.write(f'{message}\n')
        elif out_type == 'error':
            sys.stderr.write(message)
        elif out_type == 'stdin':
            sys.stdin.write(message)
