from os import system
from time import sleep
from random import choice
from string import ascii_letters, digits

system('title [Password Generator]')
clear = lambda: system('cls')
clear()

while True:
    while True:
        try:
            amount = int(input('Amount of characters: '))
        except ValueError:
            print('> Please input a digit.')
            sleep(2)
            clear()
            continue
        break

    note = str(input('Note: '))
    password = ''.join(choice(ascii_letters + digits + '!"#¤%&/()=?`*^@£$€{[]}\\,.-_—<>§~+|•') for _ in range(amount))
    print('> Generated Password: %s' % (password))
    with open('Passwords.txt', 'a', encoding='UTF-8') as f:
        f.write('Password: %s | Note: %s\n' % (password, note))
    print()
