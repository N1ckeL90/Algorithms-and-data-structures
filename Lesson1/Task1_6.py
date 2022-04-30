# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
letter_num = int(input('Введите номер буквы в алфавите: '))
letter = alphabet[letter_num - 1]
print(letter)
