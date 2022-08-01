from random import randint
from string import *

chars = {'ascii_low': (ascii_lowercase, 'Латинские буквы нижний регистр'),
         'ascii_up': (ascii_uppercase, 'Латинские буквы верхний регистр'),
         'digits': (digits, 'Цифры'),
         'symbols': ('%,*,),?,@,#,$,~', 'Специальные символы'),
         }


class RandPassword:
    def __init__(self, chars):
        self.__chars = chars

    def __call__(self, num):
        result = set()
        while len(result) < num:
            result.add(self.__chars[randint(0, len(self.__chars)-1)])

        return ''.join(list(result))

    # return ''.join([self.__chars[randint(0, len(self.__chars) - 1)] for _ in range(num)])