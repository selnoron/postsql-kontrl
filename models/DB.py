import psycopg2
from decimal import Decimal


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
                dbname='forum'
            )
            conn.autocommit = True
            return conn
        except Exception as e:
            return e + '\n' + "[ERROR] CONNECTION ERROR!"

    @staticmethod
    def get_user(login: str) -> str:
        conn = DB.connect()
        try:
            with conn.cursor() as cur:
                cur.execute(f"SELECT id FROM users WHERE login='{login}'")
                rows = cur.fetchall()
            result = rows[0]
            return result[0]
        except:
            return 1
        
    @staticmethod
    def get_users_root(login: str) -> str:
        conn = DB.connect()
        user_id = DB.get_user(login)
        try:
            with conn.cursor() as cur:
                cur.execute(f'''
                            SELECT id FROM authors
                            WHERE user_id = {user_id}
                            ''')
                rows = cur.fetchall()
            result = [2]
            if rows:
                result[0] = 1
                result.append(rows[0][0])
            result.append('no')
            return result
        except:
            return 123
        
    @staticmethod
    def get_all_artcs() -> str:
        conn = DB.connect()
        try:
            with conn.cursor() as cur:
                cur.execute(f"SELECT * FROM articles;")
                rows = cur.fetchall()
            result = []
            res = []
            for row in rows:
                res = []
                for ro in row:
                    res.append(ro)
                result.append(res)
            return result
        except:
            return 1
        
    @staticmethod
    def get_rate_of_art(id: int) -> str:
        conn = DB.connect()
        try:
            with conn.cursor() as cur:
                cur.execute(f"SELECT AVG(rate) FROM ratings WHERE article_id={id};")
                rows = cur.fetchall()
            result = rows[0][0].quantize(Decimal("1.00"))
            print(result)
            return result
        except:
            return 1
        
    @staticmethod
    def get_all_ratings() -> str:
        conn = DB.connect()
        try:
            with conn.cursor() as cur:
                cur.execute(f"SELECT users.full_name, article_id, rate, text FROM ratings INNER JOIN users ON users.id = ratings.user_id;")
                rows = cur.fetchall()
            result = []
            res = []
            for row in rows:
                res = []
                for ro in row:
                    res.append(ro)
                result.append(res)
            return result
        except:
            return 1
    
    @staticmethod
    def get_users_data(login: str) -> str:
        conn = DB.connect()
        try:
            with conn.cursor() as cur:
                cur.execute(f"SELECT id, login, full_name FROM users WHERE login='{login}';")
                rows = cur.fetchall()
            result = []
            for row in rows:
                for ro in row:
                    result.append(ro)
            return result
        except:
            return 1
        
    @staticmethod
    def auth_user(login: str) -> str:
        conn = DB.connect()
        try:
            with conn.cursor() as cur:
                cur.execute(f"SELECT password FROM users WHERE login='{login}'")
                rows = cur.fetchall()
            result = rows[0]
            return result
        except:
            return 1

    @staticmethod
    def insert_users(login: str, full_name: str, password: str) -> str:
        conn = DB.connect()
        try:
            with conn.cursor() as cur:
                cur.execute(query=f'''
                            INSERT INTO users (login, full_name, password) 
                            VALUES ('{login}', '{full_name}', '{password}');
                            ''')
            return 0
        except Exception as exc:
            return exc
    
    @staticmethod
    def insert_authors(user_id: int) -> str:
        conn = DB.connect()
        try:
            with conn.cursor() as cur:
                cur.execute(query=f'''
                            INSERT INTO authors (user_id) 
                            VALUES ({user_id});
                            ''')
            return 0
        except Exception as exc:
            return exc
    
    @staticmethod
    def insert_articles(title: str, text: str, author_id: int) -> str:
        conn = DB.connect()
        with conn.cursor() as cur:
            cur.execute(query=f'''
                        INSERT INTO articles (title, text, author_id) 
                        VALUES ('{title}', '{text}', {author_id});
                        ''')
        return 0
    
    @staticmethod
    def insert_ratings(user_id: int, article_id: int, rate: int, text: str) -> str:
        conn = DB.connect()
        with conn.cursor() as cur:
            cur.execute(query=f'''
                        INSERT INTO ratings (user_id, article_id, rate, text) 
                        VALUES ({user_id}, {article_id}, {rate}, '{text}');
                        ''')
        return 0
        
    
    @staticmethod
    def create() -> str:
        conn = DB.connect()
        try:
            with conn.cursor() as cur:
                cur.execute(f'''
                            CREATE TABLE IF NOT EXISTS users (
                                id SERIAL PRIMARY KEY, 
                                login VARCHAR(30) UNIQUE,
                                full_name VARCHAR(120),
                                password VARCHAR(10)
                            );
                            CREATE TABLE IF NOT EXISTS authors (
                                id SERIAL PRIMARY KEY, 
                                user_id INTEGER REFERENCES users(id)
                            );
                            CREATE TABLE IF NOT EXISTS articles (
                                id SERIAL PRIMARY KEY, 
                                title VARCHAR(30),
                                text TEXT,
                                author_id INTEGER REFERENCES authors(id)
                            );
                            CREATE TABLE IF NOT EXISTS ratings (
                                user_id INTEGER REFERENCES users(id),
                                article_id INTEGER REFERENCES articles(id),
                                rate INTEGER CHECK(rate <= 10 AND rate >= 0),
                                text VARCHAR(500)
                            );
                            '''
                            )
            return 0
        except:
            return 1