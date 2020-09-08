from psycopg2.pool import SimpleConnectionPool
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData

from collections import Iterable
from core.models import BaseDAO


class AlchemyService:
    def __init__(self):
        self.__db_url = 'postgresql://app_user:@pp_u53r@localhost:5432/test_db'
        self.__conn = None
        self.__session = None
        self.__engine = None
        self.__connect()
        self.__migrate()

    def __connect(self):
        self.__engine = create_engine(self.__db_url, echo=True)
        self.__conn = self.__engine.connect()
        self.__session = sessionmaker(bind=self.__engine)()

    def save(self, data_obj):

        if isinstance(data_obj, Iterable):
            self.__session.add_all(data_obj)
        else:
            self.__session.add(data_obj)
        try:
            self.__session.commit()
        except Exception as e:
            self.__session.rollback()
            raise e
        finally:
            self.__session.close()

    def __migrate(self):
        BaseDAO.Base.metadata.create_all(self.__engine)


class ConnectionPool:
    """
    Service class to get a connection and
    to return a connection to the pool
    """
    __con_pool = None

    @classmethod
    def create_pool(cls, **kwargs):
        cls.__con_pool = SimpleConnectionPool(1, 5, **kwargs)

    @classmethod
    def get_connection(cls):
        return cls.__con_pool.getconn()

    @classmethod
    def return_connection(cls, connection):
        cls.__con_pool.putconn(connection)

    @classmethod
    def close_all_connection(cls):
        cls.__con_pool.closeall()


class DatabaseConnection:
    """
    Context manager to get connection from connection pool and
    return the connection to connection pool.
    """
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
