from localization import BaseLanguage


def check_results(language: BaseLanguage, player: int, computer: int) -> str:
    """Подсчет результатов"""
    if player == computer:
        return language.equal()
    elif (player == 0 and computer == len(language.dict) - 1) or (
            player > computer and not (player == len(language.dict) - 1 and computer == 0)):
        return language.win()
    return language.lost()
