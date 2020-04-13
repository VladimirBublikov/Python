# кол-во гласных букв
def glasniecount(s):
    vowels = list("aeiouyаоуеёиюэыя")
    word_set = list(s.lower())
    return sum(letter in vowels for letter in word_set)


# читаем файл в список
file = open("1.txt", encoding="utf8")
textlist = file.readlines()
file.close()

# ищем строку в которой больше всего гласных букв
maxi = 0
maxs = 0
for i in range(len(textlist)):
    if maxs < glasniecount(textlist[i]):
        maxs = glasniecount(textlist[i])
        maxi = i

# убираем из списка эту строку
textlist.pop(maxi)

# пишем копию в новый файл, без этой строки
file = open("2.txt", "w", encoding="utf8")
file.writelines(textlist)
file.close()

print("Строка, в которой больше всего гласных букв: ", maxi+1)
