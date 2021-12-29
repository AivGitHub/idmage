import os

from settings import PATH_ENVIRONMENTS

from idmage.utils import IDmageUtils


try:
    os.environ['PATH_ENVIRONMENTS']
except KeyError:
    os.environ['PATH_ENVIRONMENTS'] = PATH_ENVIRONMENTS
