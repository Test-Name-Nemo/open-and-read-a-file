with open('1.txt', 'r', encoding='utf=8'
          ) as file_1, open('2.txt', 'r', encoding='utf=8') as file_2:
    
    files, files_2 = ['1.txt', '2.txt']
    file_contents = []
    count = 0
    for line in file_1:
        count += 1
        file_contents.append((files, count, len(line), line))
        
        file_1.readline()

    for line in file_2:
        count = 1
        file_contents.append((files_2, count, len(line), line))
        file_2.readline()

    file_contents.sort(key=lambda x: x[2])

    print(file_contents)

with open('result.txt', 'w', encoding='utf=8') as f:
    for file in file_contents:
        f.write(file[0] + '\n')
        f.write(str(file[1]) + '\n')
        f.write(file[3])

print("Файлы объединены и отсортированы в файле result.txt")