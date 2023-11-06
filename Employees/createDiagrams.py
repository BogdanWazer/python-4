import openpyxl
import matplotlib.pyplot as plt

# відкриття XLSX файлу
try:
    wb = openpyxl.load_workbook('employees.xlsx')
    sheet = wb['all']
except FileNotFoundError:
    print('Помилка: файл XLSX не знайдено.')
except Exception as e:
    print(f'Помилка при відкритті файлу XLSX: {str(e)}')

# Перевірка на наявність даних на аркуші
if 'sheet' in locals():
    print('Ok')

    # Ініціалізуємо лічильники для статі і вікових категорій
    gender_counts = {'Чоловіча': 0, 'Жіноча': 0}
    age_category_counts = {'0-18': 0, '19-45': 0, '46-70': 0, '71+': 0}
    gender_age_counts = {'Чоловіча': {'0-18': 0, '19-45': 0, '46-70': 0, '71+': 0},
                         'Жіноча': {'0-18': 0, '19-45': 0, '46-70': 0, '71+': 0}}

    # Визначення вікових категорій
    age_categories = {'0-18': (0, 18), '19-45': (19, 45),
                      '46-70': (46, 70), '71+': (71, float('inf'))}

    # Прочитаємо дані з аркушу і зробимо розрахунки
    for row in sheet.iter_rows(min_row=2, values_only=True):
        gender = row[3]  # Стовпець "Стать"
        age = int(row[10])  # Стовпець "Вік" перетворюємо в ціле число

        # Розрахунок кількості співробітників за статтею
        if gender == 'Чоловіча':
            gender_counts['Чоловіча'] += 1
        elif gender == 'Жіноча':
            gender_counts['Жіноча'] += 1

        # Розрахунок вікової категорії
        for category, (min_age, max_age) in age_categories.items():
            if min_age <= age <= max_age:
                age_category_counts[category] += 1

        # Розрахунок кількості співробітників жіночої та чоловічої статі відповідно до віку
        gender_age_counts[gender]['0-18'] += 1 if 0 <= age <= 18 else 0
        gender_age_counts[gender]['19-45'] += 1 if 19 <= age <= 45 else 0
        gender_age_counts[gender]['46-70'] += 1 if 46 <= age <= 70 else 0
        gender_age_counts[gender]['71+'] += 1 if age >= 71 else 0

    # Вивести результати
    print('\nКількість співробітників чоловічої та жіночої статі:')
    print(gender_counts)

    print('\nКількість співробітників в кожній віковій категорії:')
    print(age_category_counts)

    print('\nКількість співробітників жіночої та чоловічої статі в кожній віковій категорії:')
    print(gender_age_counts)

    # Побудова діаграм для кількості співробітників за статтею
    plt.figure(figsize=(8, 4))
    plt.bar(gender_counts.keys(), gender_counts.values())
    plt.title('Кількість співробітників за статтею')
    plt.xlabel('Стать')
    plt.ylabel('Кількість')
    plt.show()

    # Побудова діаграм для кількості співробітників в кожній віковій категорії
    plt.figure(figsize=(8, 4))
    plt.bar(age_category_counts.keys(), age_category_counts.values())
    plt.title('Кількість співробітників в кожній віковій категорії')
    plt.xlabel('Вікова категорія')
    plt.ylabel('Кількість')
    plt.show()

    # Побудова діаграм для кількості співробітників жіночої та чоловічої статі в кожній віковій категорії
    for gender in gender_age_counts.keys():
        gender_age_data = [gender_age_counts[gender][age_category]
                           for age_category in age_categories.keys()]
        plt.figure(figsize=(8, 4))
        plt.bar(age_categories.keys(), gender_age_data)
        plt.title(
            f'Кількість співробітників {gender.lower()} статі в кожній віковій категорії')
        plt.xlabel('Вікова категорія')
        plt.ylabel('Кількість')
        plt.show()
