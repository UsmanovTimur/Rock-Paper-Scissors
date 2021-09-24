# coding:utf-8
from abc import abstractmethod

__all__ = ['BaseLanguage']


class BaseLanguage:
    """Базовый класс локализации"""

    def __call__(self, *args, **kwargs):
        return self.__class__()

    @abstractmethod
    def get_name(self) -> str:
        """Получение название языка"""
        pass

    @abstractmethod
    def hello(self) -> str:
        """
        Приветсвенное слово
        :return:
        """
        pass

    @abstractmethod
    def get_rock(self) -> str:
        """Получение имени камень"""
        pass

    @abstractmethod
    def get_paper(self) -> str:
        """Получение имени бумаги"""
        pass

    @abstractmethod
    def question(self) -> str:
        """вопрос пользователю"""
        pass

    @abstractmethod
    def again_question(self) -> str:
        """вопрос пользователю о повторе игры"""
        pass

    @abstractmethod
    def user_chose(self) -> str:
        """выбор пользователя"""
        pass

    @abstractmethod
    def computer_chose(self) -> str:
        """выбор компьютера"""
        pass

    @abstractmethod
    def get_scissor(self) -> str:
        """Получение имени ножниц"""
        pass

    @abstractmethod
    def win(self) -> str:
        """Победа"""
        pass

    @abstractmethod
    def lost(self) -> str:
        """Проигрыш"""
        pass

    @abstractmethod
    def equal(self) -> str:
        """ничья"""
        pass

    @property
    def list(self):
        """Получение списка вариантов"""
        return enumerate([self.get_rock(), self.get_paper(), self.get_scissor()])

    @property
    def dict(self):
        """Получение списка вариантов в виде словаря"""
        return {k: v for k, v in self.list}
