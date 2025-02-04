# Домашнее задание по теме "Введение в потоки".
# Задача "Потоковая запись в файлы"

from time import sleep
from datetime import datetime
from threading import Thread

def write_words(word_count, file_name):
    file = open(file_name, 'w', encoding='utf-8')
    for i in range(word_count):
        file.write(f'Какое-то слово № {i+1}\n')
        sleep(0.1)
    file.close()
    print(f'Завершилась запись в файл {file_name}')

time_start_1 = datetime.now()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

time_stop_1 = datetime.now()
time_res_1 = time_stop_1 - time_start_1

print(f'Время работы функции {time_res_1}')

time_start_2 = datetime.now()

thread_one = Thread(target=write_words, args=(10, 'example5.txt'))
thread_two = Thread(target=write_words, args=(30, 'example6.txt'))
thread_three = Thread(target=write_words, args=(200, 'example7.txt'))
thread_four = Thread(target=write_words, args=(100, 'example8.txt'))

thread_one.start()
thread_two.start()
thread_three.start()
thread_four.start()

thread_one.join()
thread_two.join()
thread_three.join()
thread_four.join()

time_stop_2 = datetime.now()
time_res_2 = time_stop_2 - time_start_2

print(f'Время работы ПОТОКОВ {time_res_2}')

time_res = time_res_1 - time_res_2

print(f'Время  работы ПОТОКОВ функции быстрее работы функций на {time_res}')
