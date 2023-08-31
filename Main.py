import random

print('Your password: ')
chars = 'abcdeefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_'
password = ''
for x in range(16):
    password += random.choice(chars)

print(password)