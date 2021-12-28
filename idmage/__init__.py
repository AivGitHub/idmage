import os

from settings import PATH_ENVIRONMENTS


try:
    os.environ['PATH_ENVIRONMENTS']
except KeyError:
    os.environ['PATH_ENVIRONMENTS'] = PATH_ENVIRONMENTS
