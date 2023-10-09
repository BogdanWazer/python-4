import csv
from faker import Faker

fake = Faker()

# задаю кількість записів
num_records = 2000

# задаю відсоток жіночої та чоловічої статі
num_female = int(0.4 * num_records)
num_male = int(0.6 * num_records)

# задаю діапазон для року народження (від 1938 до 2008 року)
start_birth_year = 1938
end_birth_year = 2008

# генерація та збереження даних
with open('employees.csv', 'w', newline='') as csvfile:
    fieldnames = ['Прізвище', 'Ім’я', 'Стать', 'Дата народження', 'Посада', 'Місто проживання', 'Адреса проживання', 'Телефон', 'Email'] # прописання назви полів
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames) # запис даних
    
    writer.writeheader()
    
    for _ in range(num_female): # _ заміняє індекс, щоб його не використовувати взагалі
        gender = 'Жіноча'
        birth_date = fake.date_of_birth(tzinfo=None, minimum_age=2023 - end_birth_year, maximum_age=2023 - start_birth_year)
        writer.writerow({
            'Прізвище': fake.last_name(),
            'Ім’я': fake.first_name_female(),
            'Стать': gender,
            'Дата народження': birth_date.strftime('%d/%m/%Y'),
            'Посада': fake.job(),
            'Місто проживання': fake.city(),
            'Адреса проживання': fake.address(),
            'Телефон': fake.phone_number(),
            'Email': fake.email()
        })
    
    for _ in range(num_male):
        gender = 'Чоловіча'
        birth_date = fake.date_of_birth(tzinfo=None, minimum_age=2023 - end_birth_year, maximum_age=2023 - start_birth_year)
        writer.writerow({
            'Прізвище': fake.last_name(),
            'Ім’я': fake.first_name_male(),
            'Стать': gender,
            'Дата народження': birth_date.strftime('%d/%m/%Y'),
            'Посада': fake.job(),
            'Місто проживання': fake.city(),
            'Адреса проживання': fake.address(),
            'Телефон': fake.phone_number(),
            'Email': fake.email()
        })

print(f'Згенеровано {num_records} записів у файл "employees.csv"') # виводимо результати
