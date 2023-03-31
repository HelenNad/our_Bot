import inquirer
from ab import CONFIG as ab_config
from note import CONFIG as nb_config
from clean import CONFIG as sa_config
from header import Handler


main_menu = [
    inquirer.List('option',
                  message='You are in main menu. Please select an option:',
                  choices=[
                      'Address Book',
                      'Note Book',
                      'Sorter Assist',
                      'Exit'
                  ])
]


def main():
    while True:
        main_choice = inquirer.prompt(main_menu)['option']

        if main_choice == 'Address Book':
            handler = Handler(**ab_config)
            handler.run()

        elif main_choice == 'Note Book':
            handler = Handler(**nb_config)
            handler.run()

        elif main_choice == 'Sorter Assist':
            handler = Handler(**sa_config)
            handler.run()
        elif main_choice == 'Exit':
            print("Exiting program...")
            break


if __name__ == '__main__':
    main()
