from localization import BaseLanguage
from computer_choice import computer_choice
from check_results import check_results


def play(language: BaseLanguage):
    try:
        player_result = int(input(f'{language.question()} '))
    except:
        print("Incorrect input")
        return
    computer_result = computer_choice()

    # viusual representation in the terminal so we can see what both parties chose
    print(f'{language.user_chose():15}: {language.dict[player_result]}')
    print(f'{language.computer_chose():15}: {language.dict[computer_result]}')

    # check the results between the two and print the winner.
    results = check_results(language, player_result, computer_result)
    print(f'\n{results}')
