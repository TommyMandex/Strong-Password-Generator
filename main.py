from os import system
from time import sleep
from random import choice
from string import ascii_letters, digits, punctuation

system('cls && title [Password Generator]')

while True:
    bypassed = False
    while not bypassed:
        try:
            amount = int(input('Amount of characters: '))
        except ValueError:
            print('> Please input a digit.')
            sleep(2)
            system('cls')
            continue
        bypassed = True

    note = str(input('Note: '))
    password = ''.join(choice(
        ascii_letters + digits + punctuation + '¤£€—§•'
    ) for _ in range(amount))
    print('> Generated Password: %s' % password)
    with open('Passwords.txt', 'a', encoding='UTF-8') as f:
        f.write('Password: %s | Note: %s\n' % (password, note))
    print()
