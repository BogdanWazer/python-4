import pandas as pd
from datetime import datetime

# Завантаження даних з CSV файлу
try:
    df = pd.read_csv('employees.csv', encoding='utf-8')
except FileNotFoundError:
    print('Помилка: файл CSV не знайдено.')
    exit(1)
except Exception as e:
    print(f'Помилка при завантаженні CSV файлу: {str(e)}')
    exit(1)

# Перевірка наявності стовпця "Дата народження"
if 'Дата народження' in df.columns:
    # Перетворення стовпця "Дата народження" у тип datetime.date
    df['Дата народження'] = pd.to_datetime(
        df['Дата народження'], format='%d/%m/%Y', errors='coerce').dt.date

    # Видалення рядків з некоректною датою
    df = df.dropna(subset=['Дата народження'])

    # Функція для обчислення віку з урахуванням місяців
    def calculate_age(birth_date):
        today = datetime.now()
        age = today.year - birth_date.year - \
            ((today.month, today.day) < (birth_date.month, birth_date.day))
        return age

    # Обчислення віку з урахуванням місяців
    df['Вік'] = df['Дата народження'].apply(calculate_age)

    # Створення XLSX файлу
    try:
        with pd.ExcelWriter('employees.xlsx', engine='xlsxwriter') as writer:
            # Аркуш "all"
            df.to_excel(writer, sheet_name='all', index=False)

            # Аркуши з віковими категоріями
            age_bins = [0, 18, 45, 70, float('inf')]
            age_labels = ['younger_18', '18-45', '45-70', 'older_70']

            for i in range(len(age_bins) - 1):
                age_range_df = df[(df['Вік'] > age_bins[i])
                                  & (df['Вік'] <= age_bins[i+1])]
                age_range_df[['Прізвище', 'Ім’я', 'Дата народження', 'Вік']].to_excel(
                    writer, sheet_name=age_labels[i], index=False)

        print('Ok, програма завершила свою роботу успішно.')
    except Exception as e:
        print(f'Помилка: неможливо створити XLSX файл. {str(e)}')
else:
    print('Помилка: стовпець "Дата народження" відсутній у файлі.')
