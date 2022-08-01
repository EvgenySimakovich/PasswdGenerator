import os
import signal

from pywebio.input import *
from pywebio.output import *
from pywebio import start_server
from pywebio.session import run_js

from rand import *


def valid_lenght_passwd(lenght):
    if lenght < 5 or lenght > 15:
        return 'Пароль должен содержать от 5 до 15 символов'


def valid_check_chars(checker):
    if checker == []:
        return 'Нужно выбрать хотя бы один пункт'


def valid_check_lenght(data):
    if len(''.join([chars[item][0] for item in data['check_chars']])) < data['lenght_passwd']:
        return ('lenght_passwd', 'Символы в пароле не повторяются. '
                                 'Измените длину пароля или выберите дополнительные группы символов.')


def main():
    put_markdown('Генератор паролей (Версия 1.0)')
    data = input_group('Настройки генератора', [
        checkbox("Допустимые символы: ", options=[
            ('Латинские буквы нижний регистр', 'ascii_low'),
            ('Латинские буквы верхний регистр', 'ascii_up'),
            ('Цифры', 'digits'),
            ('Специальные символы  %, *, ), ?, @, #, $, ~', 'symbols')
        ], name='check_chars', validate=valid_check_chars),
        input(type=NUMBER, name='lenght_passwd', validate=valid_lenght_passwd, placeholder='Длина пароля (от 5 до 15)'),
    ], validate=valid_check_lenght)

    passwd = RandPassword(''.join([chars[item][0] for item in data['check_chars']]))

    put_grid([
        [put_markdown('Пароль: ', cell_width='100px'), passwd(data['lenght_passwd']), None],
        ['Длина пароля: ', data['lenght_passwd'], None],
        ['Символы: ', span(put_text(*[chars[item][1] for item in data['check_chars']], sep='\n'), col=2, row=1)],
        ], cell_width='150px')
    put_text('Спасибо за выбор приложения "Генератор паролей"!\n'
             'Оставьте Ваши пожелания при себе.')

    put_buttons(['Заново',
                 {'label': 'Завершить', 'color': 'danger', 'value': 'close_btn'}], onclick=[
        lambda: run_js('window.location.reload()'),
        lambda: os.kill(os.getpid(), signal.SIGTERM)
    ])


if __name__ == '__main__':
    start_server(main, port=8080, debug=True)