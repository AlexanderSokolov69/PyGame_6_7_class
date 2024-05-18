def decode(data):
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    sp = [int(x) - 1 for x in data.split()]
    slovo = ''.join([alphabet[n] for n in sp])
    return slovo

    
print(decode(input()))
