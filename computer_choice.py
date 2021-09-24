from random import randint

__all__ = ['computer_choice']


def computer_choice():
    """
    Выбор комьпьютера
    :return:
    """
    computer_chose = randint(0, 2)
    return computer_chose
