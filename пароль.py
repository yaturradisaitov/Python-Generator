import random
import string

def generate_password(length, use_digits=True, use_special=True):
    chars = string.ascii_letters
    if use_digits:
        chars += string.digits
    if use_special:
        chars += string.punctuation

    return ''.join(random.choice(chars) for _ in range(length))

length = int(input("Введите длину пароля: "))
use_digits = input("Добавить цифры? (y/n): ").lower() == 'y'
use_special = input("Добавить спецсимволы? (y/n): ").lower() == 'y'

print("Ваш случайный пароль:", generate_password(length, use_digits, use_special))
