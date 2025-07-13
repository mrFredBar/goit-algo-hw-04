#4.1
# Ваше завдання - розробити функцію total_salary(path), яка аналізує цей файл і повертає загальну та середню суму заробітної плати всіх розробників.
import os
from pathlib import Path
print("Текущая папка:", os.getcwd())#Проверял путь к файлу так как у меня просто раньше не видел его

def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            total = 0
            count = 0

            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 2:
                    try:
                        salary = float(parts[1])
                        total += salary
                        count += 1
                    except ValueError:
                        continue

            average = total / count if count > 0 else 0
            return total, average
    except FileNotFoundError:
        print("Файл не найден.")
        return 0, 0

total, average = total_salary(Path(r'c:\Users\danil\Desktop\4.1\Money.txt'))

print("Загальна сума заробітної плати:", total)
print("Середня сума заробітної плати:", average)