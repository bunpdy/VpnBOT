import sqlite3
from sqlite3 import Error

def create_connection():
    """Создаем соединение с SQLite базой данных"""
    conn = None
    try:
        conn = sqlite3.connect('users.db')  # Создаст файл users.db
        print(f"Подключение к SQLite успешно, версия SQLite: {sqlite3.version}")
        return conn
    except Error as e:
        print(f"Ошибка при подключении к SQLite: {e}")
    return conn

def create_table(conn):
    """Создаем таблицу пользователей, если её нет"""
    print("Создаем таблицу пользователей, если её нет")
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                user_id INTEGER UNIQUE,
                full_name TEXT,
                username TEXT,
                reg_date TEXT,
                balance INTEGER,
                subscription_start_date DATE
            )
        ''')
        conn.commit()
    except Error as e:
        print(f"Ошибка при создании таблицы: {e}")

def add_user(conn, user_id, full_name, username, reg_date):
    """Добавляем пользователя в базу данных"""
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT OR IGNORE INTO users (user_id, full_name, username, reg_date, balance, subscription_start_date)
            VALUES (?, ?, ?, ?, 0, NULL)
        ''', (user_id, full_name, username, reg_date))
        conn.commit()
        return cursor.lastrowid
    except Error as e:
        print(f"Ошибка при добавлении пользователя: {e}")
    return None

def get_user_balance(conn, user_id: int) -> int:
    """Получает баланс пользователя по его user_id"""
    cursor = conn.cursor()
    cursor.execute("SELECT balance FROM users WHERE user_id = ?", (user_id,))
    result = cursor.fetchone()
    return result[0] if result else 0

def activate_subscription(user_id: int, duration_days: int):
    pass
    # # Текущая дата
    # start_date = datetime.now().date()
    # end_date = start_date + timedelta(days=duration_days)

    # cursor = conn.cursor()
    # cursor.execute("""
    #     UPDATE users 
    #     SET subscription_start_date = ?, subscription_end_date = ?
    #     WHERE user_id = ?
    # """, (start_date, end_date, user_id))
    # conn.commit()

def get_subscription_days(conn):
    cursor = conn.cursor()
    pass

# Инициализация базы данных при импорте
conn = create_connection()
if conn is not None:
    create_table(conn)
else:
    print("Ошибка! Не удалось подключиться к базе данных")
