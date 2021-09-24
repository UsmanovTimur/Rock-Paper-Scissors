from dataclasses import dataclass
from localization import LANGUAGES, BaseLanguage

__all__ = ['select_language', 'HelloStrategy']


def select_language(language: str) -> BaseLanguage:
    """
    Выбор языка для игры
    :return:
    """
    return LANGUAGES.get(language.lower())() if LANGUAGES.get(language.lower()) is not None else None


@dataclass
class HelloStrategy:
    """
    Приветственное слово
    :return:
    """
    language: BaseLanguage

    def say_hello(self):
        print(self.language.hello().format("\n".join([f"{v:10}: {k}" for k, v in self.language.list])))
