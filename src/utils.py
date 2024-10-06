import psycopg2


def create_database(params, database_name):
    """Создает новую базу данных."""
    conn = None
    try:
        conn = psycopg2.connect(**params)
        conn.autocommit = True  # Включаем режим автокоммита
        with conn.cursor() as cur:
            cur.execute(f"SELECT 1 FROM pg_database WHERE datname = '{database_name}'")
            exists = cur.fetchone()
            if not exists:
                cur.execute(f"CREATE DATABASE {database_name}")
                print(f'БД "{database_name}" успешно создана"')
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Ошибка: {error}")
    finally:
        if conn is not None:
            conn.close()

def execute_sql_script(script_file, cur):
    """Выполняет скрипт из файла для заполнения БД данными."""
    with open(script_file, 'r', encoding='utf-8') as f:
        sql_script = f.read()
    cur.execute(sql_script)

def create_suppliers_table(cur):
    """Создает таблицу suppliers."""
    cur.execute("CREATE TABLE IF NOT EXISTS suppliers(company_name VARCHAR(100), contact VARCHAR(100),"
                "address VARCHAR(100), phone VARCHAR(20), fax VARCHAR(20), homepage VARCHAR(255), products JSONB)")

def get_suppliers_data(json_file):
    """Извлекает данные о поставщиках из JSON-файла и возвращает список словарей с соответствующей информацией."""
    pass

def insert_suppliers_data(cur, suppliers):
    """Добавляет данные из suppliers в таблицу suppliers."""
    pass

def add_foreign_keys(cur, json_file):
    """Добавляет foreign key со ссылкой на supplier_id в таблицу products."""
    pass
