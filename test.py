# получим объект файла
with open("pass.txt", "r") as file1:
    # итерация по строкам
    for line in file1:
        print(line.strip())
