from typing import Self
import psycopg2


class Connection:
    """
    Connection with PostgreSQl.
    """

    def __new__(cls, *args, **kwargs) -> Self:
        if not hasattr(cls, 'instance'):
            cls.instance = super(
                Connection, cls
            ).__new__(cls)
        return cls.instance

    def __init__(
        self,
        host: str,
        port: int,
        user: str,
        password: str,
        dbname: str
    ) -> None:
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.dbname = dbname
        self.conn = None
        try:
            self.conn = psycopg2.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                dbname=self.dbname,
            )
            print('[SUCCESS] Connection is success!')
        except Exception as e:
            print(e)
            print("[ERROR] CONNECTION ERROR!")