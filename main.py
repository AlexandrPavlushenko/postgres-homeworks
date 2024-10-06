from config import config
from src.utils import *

script_file = 'fill_db.sql'
json_file = 'suppliers.json'
db_name = 'my_new_db'

params = config()
conn = None

create_database(params, db_name)
params.update({'dbname': db_name})

try:
    conn = psycopg2.connect(**params)
    conn.autocommit = True
    with conn.cursor() as cur:
        execute_sql_script(script_file, cur)
        create_suppliers_table(cur)

except (Exception, psycopg2.DatabaseError) as e:
    print(f"Ошибка: {e}")
finally:
    if conn is not None:
        conn.close()
