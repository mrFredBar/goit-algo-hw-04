#4.2

#Функция получает информацию о кошках из файла cats.txt и вносит их в словарь
def get_cats_info(path):
    cats_info = []
    try:
        with open(path, "r") as file:
            for line in file:
                id, name, age = line.strip().split(",")
                cats_info.append({"id": id, "name": name, "age": int(age)})
    except FileNotFoundError:
        print(f"File not found: {path}")
    return cats_info





#Получение данных через функцию и вывод информации через цикл для лучшего понимания информации, так как в файле cats.txt, в каждой строке
cats_info = get_cats_info("cats.txt")
for cat in cats_info:
    print (cat)