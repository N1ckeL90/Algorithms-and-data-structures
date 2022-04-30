# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
first_letter = input('Введите первую букву: ')
second_letter = input('Введите вторую букву: ')
#находим позиции букв в алфавите
first_index = alphabet.index(first_letter) + 1
second_index = alphabet.index(second_letter) + 1
#подсчет количества букв между ними (по модулю)
distance = abs(second_index - first_index) - 1
print(f'Позиция буквы "{first_letter}" - {first_index}\n'
      f'Позиция буквы "{second_letter}" - {second_index}\n'
      f'Количество букв между ними - {distance}')
