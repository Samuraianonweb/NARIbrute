with open("pass.txt", encoding="utf-8") as file:
 id = [l.strip() for l in file]
for pars in id:
print(pars)
