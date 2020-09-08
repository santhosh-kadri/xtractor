from dataclasses import dataclass
from sqlalchemy.ext.declarative import declarative_base

@dataclass
class BaseDAO:
    """Base DAO to handle SQLAlchemy orm.
    """
    Base = declarative_base()
