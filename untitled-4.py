def num_of_letter(sym):
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    n = alphabet.find(sym) + 1
    return n


print(num_of_letter(input()))
