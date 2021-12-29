import argparse
import sys

from idmage.maintain import Maintain


def run():
    parser = argparse.ArgumentParser(description='Process images.')

    parser.add_argument('-p', '--path',
                        required=True,
                        nargs=1,
                        help='Path to image file')

    parser.add_argument('-d', '--delete-exif',
                        required=False,
                        action='store_true',
                        help='Remove exif data')

    parser.add_argument('-q', '--quiet',
                        required=False,
                        help='No stdout',
                        action='store_true')

    parser.add_argument('-r', '--recursive',
                        required=False,
                        help='Recursive',
                        action='store_true')

    parser.add_argument('-m', '--message',
                        required=not {'--steganography', '-s'}.isdisjoint(set(sys.argv)),
                        help='Message to hide')

    parser.add_argument('-s', '--steganography',
                        required=not {'--message', '-m'}.isdisjoint(set(sys.argv)),
                        action='store_true',
                        help='Flag to hide text in image')

    args = parser.parse_args()
    dict_args = vars(args)

    maintain = Maintain(**dict_args)
    maintain.process()


if __name__ == '__main__':
    run()
