from random import choices
import string


def what_to_use(choce):
    number = ''.join(choices(string.digits, k=9))
    letter = ''.join(choices(string.ascii_letters, k=9))
    mix = ''.join(choices(string.ascii_letters + string.digits, k=9))
    match choce:
        case '1':
            pwd = ('-'.join([letter[:3], letter[3:6], letter[6:]]))
        case '2':
            pwd = ('-'.join([number[:3], number[3:6], number[6:]]))
        case '3':
            pwd = ('-'.join([mix[:3], mix[3:6], mix[6:]]))
        case _:
            pwd = "Некорректный выбор"
    return pwd


def main():
    print('Пароль будет в формате xxx-xxx-xxx')
    print('1 если хотите использовать только буквы\n'
          '2 если хотите использовать только цифры\n'
          '3 если и то и другое')
    choce = input('-->')
    print('Вот ваш пароль')
    print(what_to_use(choce))

main()