import string
import random


class IDmageUtils(object):

    @staticmethod
    def get_random_string(quantity=10):
        return ''.join(random.choices(string.ascii_letters.lower() + string.digits, k=quantity))
