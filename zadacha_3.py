with open('1.txt', 'r', encoding='utf=8'
          ) as file_1, open('2.txt', 'r', encoding='utf=8') as file_2, open(
                                '3.txt', 'w', encoding='utf=8') as file_3:
    # file_names = ['1.txt', '2.txt'] # список имен файлов
    a = file_1.readline()
    b = file_1.readline()
    c = file_2.readline()
    file_3.write('2.txt \n')
    file_3.write('1 \n')
    file_3.write(c)
    file_3.write('\n')
    file_3.write('1.txt \n')
    file_3.write('2 \n')
    file_3.write(a)
    file_3.write(b)
