# coding:utf-8
from .localization import BaseLanguage


class RuLanguage(BaseLanguage):
    """Русский язык"""

    @classmethod
    def get_name(cls) -> str:
        return "Русский"

    def hello(self) -> str:
        return """Добрового времени суток! Приятной игры)\nВыберите вариант:\n{}"""

    def get_rock(self) -> str:
        """Получение имени камень"""
        return "Камень"

    def get_paper(self) -> str:
        """Получение имени бумаги"""
        return "Бумага"

    def get_scissor(self) -> str:
        """Получение имени ножниц"""
        return "Ножницы"

    def question(self) -> str:
        """вопрос пользователю"""
        return "Ваш выбор?"

    def again_question(self) -> str:
        """вопрос пользователю о повторе игры"""
        return "Сыграем еще?"

    def user_chose(self) -> str:
        """выбор пользователя"""
        return "выбор пользователя"

    def computer_chose(self) -> str:
        """выбор компьютера"""
        return "выбор компьютера"

    def win(self) -> str:
        """Победа"""
        return "Вы победили!!!"

    def lost(self) -> str:
        """Проигрыш"""
        return "Вы проиграли!!!"

    def equal(self) -> str:
        """ничья"""
        return "Ничья!!!"
