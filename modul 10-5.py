# Задача "Многопроцессное считывание":
# Необходимо считать информацию из нескольких файлов одновременно, используя многопроцессный подход.
# Создайте функцию read_info(name), где name - название файла. Функция должна:
# Создавать локальный список all_data.
# Открывать файл name для чтения.
# Считывать информацию построчно (readline), пока считанная строка не окажется пустой.
# Во время считывания добавлять каждую строку в список all_data.
# Используйте конструкцию if __name__ == '__main__' при многопроссном подходе.
# Выводить или возвращать список all_data в функции не нужно.
# Можете сделать это, но кол-во информации в файлах достигает - 10^9 строк.

import multiprocessing
import datetime


def read_info(name):
	all_data = []
	with open(name, 'r', encoding='utf-8') as file:
		while True:
			line = file.readline()
			all_data.append(line)
			if line == "":
				break
	file.close()

file_names = [f'./file {number}.txt' for number in range(1, 5)]

if __name__ == "__main__":
	start1 = datetime.datetime.now()
	for file_name in file_names:
		read_info(file_name)
	end1 = datetime.datetime.now()
	print(f'{end1 - start1}, Линейный процесс')

	with multiprocessing.Pool(processes=4) as pool:
		start2 = datetime.datetime.now()
		pool.map(read_info, file_names)
		end2 = datetime.datetime.now()
	print(f'{end2 - start2}, Мультипроцессность')
