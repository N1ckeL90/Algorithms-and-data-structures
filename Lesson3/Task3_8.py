matrix = []
# создаем пустую матрицу 5х4
for i in range(4):
    matrix.append([0]*5)
#заполняем с клавиатуры
i = 0
j = 0
count = 0
while count < 16:
    value = int(input('Введите число: '))
    if j == 4:
        i += 1
        j = 0
    matrix[i][j] = value
    j += 1
    count += 1
#подсчет суммы
for i in range(4):
    for j in range(4):
        matrix[i][4] += matrix[i][j]
print(matrix)
