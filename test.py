with open("myfile.txt", encoding="utf-8") as file:
 x = [l.strip() for l in file]
print(x)
