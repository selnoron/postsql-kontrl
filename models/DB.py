import psycopg2


class DB:
    '''operations with database'''
    @staticmethod
    def connect() -> None:
        try:
            conn = psycopg2.connect(
                host='localhost',
                port=5432,
                user='postgres',
                password='admin',
                dbname=''
            )
            conn.autocommit = True
            return conn
        except Exception as e:
            return e + '\n' + "[ERROR] CONNECTION ERROR!"

    @staticmethod
    def create() -> None:
        conn = DB.connect()
        try: 
            with conn.cursor() as cur:
                cur.execute('''
                    CREATE TABLE IF NOT EXISTS users (
                        id SERIAL PRIMARY KEY,
                        login
                    )
                    CREATE TABLE IF NOT EXISTS author (
                        id SERIAL PRIMARY KEY,
                        user_id INTEGER REFERENCES users(id),
                    );
                ''')

    @staticmethod
    def get_hist() -> str:
        conn = DB.connect()
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM history")
                rows = cur.fetchall()
            result = ''
            for row in rows:
                result += str(row)
            if len(result) < 1:
                return 1
            else:
                return result
        except:
            return 1

    @staticmethod
    def insert_hist(data) -> str:
        conn = DB.connect()
        try:
            with conn.cursor() as cur:
                cur.execute(f"INSERT INTO history (operation) VALUES ({data})")
            return 0
        except:
            return 1
