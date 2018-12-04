import numpy as np
import matplotlib.pyplot as plt

# np.ones - заполнение матрици размером 3 на 5 -> единицами
matrix_subcategories = np.ones((3, 5))

# np.zeros - заполнение матрици размером 3 на 1 -> нулями
matrix_categories = np.zeros((3, 1))

# matrix_subcategories [0, :] - первая строка в матрице "matrix_subcategories"
first_row = matrix_subcategories[0, :]

# sum - сумма всех єлементов в матрице
sum_first_row = sum(matrix_subcategories[0, :])

# добавление номера "1" ко всем єлементам строки "first_row" в матрице
add_to_all_element_in_matrix = first_row + 1

# пример операции над матрицей
ex = add_to_all_element_in_matrix / (sum_first_row + 1)

# ---------------------------------------------------------

# массив для сортировки
arr = [3, 1, 2, 1, 6, 2, 9, 10, 1]

# отсортированный массив от меньшего до большего
# arr = [1, 1, 1, 2, 2, 3, 6, 9, 10]
arr.sort()

# генератор списка при
# list_generator_1 = [6, 6, 9, 18, 27, 30]
list_generator_1 = [el * 3 for el in arr if el != 1]

# list_generator_2  [3, 3, 3, 6, 6, 9, 18, 27, 30]
list_generator_2 = [el * 3 for el in arr]

# ---------------------------------------------------------

# Здесь функция array принимает два аргумента: список для конвертации в массив и тип для каждого
# КОЛИЧЕСТВО ЭЛЛЕМЕНТОВ В СТРОКЕ -> ДОЛЖНО БЫТЬ ОДИНАКОВОЕ
example_array = np.array([[1, 4, 5], [1, 4, 5]], float)

# Метод shape возвращает количество строк и столбцов в матрице (ГДЕ КОЛИЧЕСТВО ЭЛЛЕМЕНТОВ В СТРОКЕ -> ОДИНАКОВОЕ)
count_row_and_coll = example_array.shape


example_arr = [1, 4, 5, 6]


y = [0, 1, 1, 0]
x1 = [0, 0, 0.15, 0.25]
plt.plot(x1, example_arr)

s = y * x1[0]

# x2 = [0.15, 0.25, 0.35, 0.45]
# x3 = [0.35, 0.45, 0.55, 0.65]
# x4 = [0.55, 0.65, 0.75, 0.85]
# x5 = [0.75, 0.85, 1, 1]

# multiplication_arr_el_to_x1 = arr * y[0]


# plt.plot(x1, y)
# plt.plot(x2, y)
# plt.plot(x3, y)
# plt.plot(x4, y)
# plt.plot(x5, y)
plt.show()

# multiplication_arr_el_to_x1 = np.dot(arr, x1[0])
