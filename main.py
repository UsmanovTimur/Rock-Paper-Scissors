# coding:utf-8
import sys
import atexit
from localization import LANGUAGES
from play import play
from say_hello import *


def say_bye():
    print("Goodbye!")


if __name__ == "__main__":
    lang = select_language(input("Select language [{}]: ".format(",".join([f"{k}" for k in LANGUAGES.keys()]))))
    if lang is None:
        print("Incorrect language")
        sys.exit(1)
    HelloStrategy(lang).say_hello()
    play_again = ''
    while play_again.lower() not in ['n', 'no', 'н', 'нет', 'exit']:
        play(lang)
        print(lang.again_question())
        play_again = input()
    atexit.register(say_bye)
