import argparse

from idmage.maintane import Maintain


def run():
    parser = argparse.ArgumentParser(description='Process images.')

    parser.add_argument('-p', '--path', required=True, nargs=1, help='Path to image file')
    parser.add_argument('-d', '--delete_exif', required=False, help='Remove exif data', action='store_true')
    parser.add_argument('-q', '--quiet', required=False, help='No stdout', action='store_true')
    parser.add_argument('-r', '--recursive', required=False, help='Recursive', action='store_true')

    args = parser.parse_args()
    dict_args = vars(args)

    maintain = Maintain(**dict_args)
    maintain.process()


if __name__ == '__main__':
    run()
