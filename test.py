# получим объект файла
file1 = open("pass.txt", "r")

while True:
    # считываем строку
    line = file1.readline()
    # прерываем цикл, если строка пустая
    if not line:
        break
    # выводим строку
    print(line.strip())

# закрываем файл
file1.close
