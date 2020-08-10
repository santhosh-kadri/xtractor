from psycopg2.pool import SimpleConnectionPool


class ConnectionPool:
    __connection_pool = None

    @classmethod
    def create_pool(cls, **kwargs):
        cls.ConnectionPool.__connection_pool = SimpleConnectionPool(
                                                minconn=1,
                                                maxconn=5,
                                                **kwargs)

    @classmethod
    def get_connection(cls):
        return cls.__connection_pool.getconn()

    @classmethod
    def return_connection(cls, connection):
        cls.__connection_pool.putconn(connection)

    @classmethod
    def close_all_connection(cls):
        cls.__connection_pool.closeall()


class DatabaseConnection:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = ConnectionPool.get_connection()
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exec_type, exc_value, exc_traceback):
        if exc_value:
            self.connection.rollback()
        else:
            self.cursor.close()
            self.connection.commit()
        ConnectionPool.return_connection(self.connection)


