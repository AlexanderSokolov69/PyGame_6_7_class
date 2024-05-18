import random as rnd


letters_big = "QWERTYUIOPASDFGHJKLZXCVBNM"
letters_small = "qwertyuiopasdfghjklzxcvbnm"
letters_nums = "12345678901234567890"
letters_ss = "!@#$^&_!@#$^&_!@#$^&_"

print("Генератор паролей - Харитон.")
print()
print("Для генерации пароля введите маску: 'Aa0# XX'")
print("A - наличие заглавных букв")
print("a - наличие строчных букв")
print("0 - наличие цифр")
print("# - наличие спецсимволов")
print("XX - (после пробела) длина пароля")
massive = ""
while True:
    mask = input("маска: ").split()
    if len(mask) == 2:
        break
    print('Ошибка в маске!')

if "A" in mask[0]:
    massive += letters_big
if "a" in mask[0]:
    massive += letters_small
if "0" in mask[0]:
    massive += letters_nums
if "#" in mask[0]:
    massive += letters_ss

password = ''.join(rnd.sample(massive, int(mask[1])))
print("Пароль:", password)
