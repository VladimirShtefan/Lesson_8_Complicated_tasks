from Library.library import Dice


def main():
    facet = input('Введите кол-во граней: ')
    if not facet.isdigit():
        print('Ошибка ввода')
        return
    facet = int(facet)
    dice = Dice(facet)
    while True:
        answer = input('Нажмите Enter чтобы бросить кубик или введите любой текст для выхода ')
        if not answer:
            print(dice.dice_throw())
        else:
            break
    answer_history = input('Хотите получить историю? Д/Н ')
    if answer_history == 'Д':
        x = input('Введите кол-во бросков для вывода истории ')
        if not x.isdigit():
            print('Не верный ввод')
            return
        history = ', '.join(dice.get_history(int(x)))
        print(history)


if __name__ == '__main__':
    main()
