import sqlite3

def create_database():
    conn = sqlite3.connect('gifts.db')
    cursor = conn.cursor()

    # Создаем таблицу
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS gifts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            gift TEXT NOT NULL,
            price REAL NOT NULL,
            status TEXT NOT NULL
        )
    ''')

    # Вставляем данные
    gifts = [
        ('Терехин Олег Александрович', 'Книга', 250, 'не куплен'),
        ('Сергей Смирнов Владимирович', 'Часы', 1500, 'не куплен'),
        ('Полков Дмитрий Владимирович', 'Игровая консоль', 50000, 'куплен'),
        ('Полков Дмитрий Валерьевич', 'Телефон', 18000, 'куплен'),
        ('Попова Татьяна Олеговна', 'Флешка', 100, 'не куплен'),
        ('Токовой Андрей Игоревич', 'ручка', 50, 'куплен'),
        ('Егоров Василий Васильевич', 'Кофеварка', 9000, 'куплен'),
        ('Васильева Мария Дмитриевна', 'Сумка', 2500, 'куплен'),
        ('Журавлева Елена Борисовна', 'Яндекс станция', 4800, 'куплен'),
        ('Зорин Виктор Валерьевич', 'кружка', 400, 'не куплен')
    ]

    cursor.executemany('''
        INSERT INTO gifts (name, gift, price, status) VALUES (?, ?, ?, ?)
    ''', gifts)

    # Сохраняем изменения
    conn.commit()
    for row in gifts:
        print(row)
    conn.close()

if __name__ == '__main__':
    create_database()
