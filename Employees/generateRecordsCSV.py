import csv
import sys
from faker import Faker
import random

fake = Faker('uk_UA')  # Використовуємо українську локаль для Faker

# Задаємо кількість записів
num_records = 2000

# Задаємо діапазон для року народження (від 1938 до 2008 року)
start_birth_year = 1938
end_birth_year = 2008

# Функція для генерації випадкового по-батькові


def generate_middle_name():
    male_middle_names = [
        "Олексійович",
        "Андрійович",
        "Васильович",
        "Іванович",
        "Петрович",
    ]

    female_middle_names = [
        "Олександрівна",
        "Андріївна",
        "Василівна",
        "Іванівна",
        "Петрівна",
    ]

    gender = random.choice(["Чоловіча", "Жіноча"])
    if gender == "Чоловіча":
        return random.choice(male_middle_names)
    else:
        return random.choice(female_middle_names)


# Встановлюємо кодування 'utf-8' для стандартного виведення
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)

# Генерація та збереження даних
with open('employees.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Прізвище', 'Ім’я', 'По-батькові', 'Стать', 'Дата народження', 'Посада',
                  'Місто проживання', 'Адреса проживання', 'Телефон', 'Email']  # прописання назви полів
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)  # запис даних

    writer.writeheader()

    for _ in range(num_records):
        gender = random.choice(["Чоловіча", "Жіноча"])
        birth_date = fake.date_of_birth(
            tzinfo=None, minimum_age=2023 - end_birth_year, maximum_age=2023 - start_birth_year)
        middle_name = generate_middle_name()
        writer.writerow({
            'Прізвище': fake.last_name(),
            'Ім’я': fake.first_name_female() if gender == 'Жіноча' else fake.first_name_male(),
            'По-батькові': middle_name,
            'Стать': gender,
            'Дата народження': birth_date.strftime('%d/%m/%Y'),
            'Посада': fake.job(),
            'Місто проживання': fake.city(),
            'Адреса проживання': fake.address(),
            'Телефон': fake.phone_number(),
            'Email': fake.email()
        })

# виводимо результати
print(f'Згенеровано {num_records} записів у файл "employees.csv"')
