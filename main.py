from random import choices
import string

print('Пароль будет в формате xxx-xxx-xxx')

class randomize:

    def __init__(self, number, letter, mix):
        self.number = number
        self.letter = letter
        self.mix = mix

    def what_to_use(self):
        print('1 если хотите использовать только буквы\n2 если хотите использовать только цифры\n3 если и то и другое')
        while True:
            choce = input('-->')
            if choce == '1':
                print('Вот ваш пароль')
                print('-'.join([self.letter[:3], self.letter[3:6], self.letter[6:]]))
                break
            elif choce == '2':
                print('Вот ваш пароль')
                print('-'.join([self.number[:3], self.number[3:6], self.number[6:]]))
                break
            elif choce == '3':
                print('Вот ваш пароль')
                print('-'.join([self.mix[:3], self.mix[3:6], self.mix[6:]]))
                break
            else:
                print('Error try again')


generate = randomize(number=''.join(choices(string.digits, k=9)), letter=''.join(choices(string.ascii_letters, k=9)), mix=''.join(choices(string.ascii_letters + string.digits, k=9)))

generate.what_to_use()
