# coding:utf-8
from .localization import BaseLanguage


class EnLanguage(BaseLanguage):
    """Английский язык"""

    @classmethod
    def get_name(cls) -> str:
        return "English"

    def hello(self) -> str:
        return """Good day! Have a nice game)\nSelect option:\n{}"""

    def get_rock(self) -> str:
        """Получение имени камень"""
        return "Rock"

    def get_paper(self) -> str:
        """Получение имени бумаги"""
        return "Paper"

    def get_scissor(self) -> str:
        """Получение имени ножниц"""
        return "Scissor"

    def question(self) -> str:
        """вопрос пользователю"""
        return "What do you choose?"

    def again_question(self) -> str:
        """вопрос пользователю о повторе игры"""
        return "Do you want to play again?"

    def user_chose(self) -> str:
        """выбор пользователя"""
        return "user chose"

    def computer_chose(self) -> str:
        """выбор компьютера"""
        return "computer chose"

    def win(self) -> str:
        """Победа"""
        return "You win!!!"

    def lost(self) -> str:
        """Проигрыш"""
        return "You lost!!!"

    def equal(self) -> str:
        """ничья"""
        return "Tie"
