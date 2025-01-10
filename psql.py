import configparser
import psycopg2

config = configparser.ConfigParser()
config.read('config.ini')

db_config = config['postgresql']

conn = psycopg2.connect(
    host=db_config['host'],
    database=db_config['database'],
    user=db_config['user'],
    password=db_config['password'],
    port=db_config['port']
)

cur = conn.cursor()

cur.execute("SELECT * FROM location")

rows = cur.fetchall()

cur.close()
conn.close()

for row in rows:
    print(row)