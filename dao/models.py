# coding=utf-8

import datetime
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import DateTime
from sqlalchemy import func

from core.models import BaseDAO as model


class StockNews(model.Base):
    __tablename__ = 'stock_news'
    id = Column(Integer, primary_key=True)
    href = Column(String, nullable=False, unique=True)
    header = Column(String, nullable=False, unique=True)
    sub_header = Column(String, nullable=False)
    source = Column(Integer, nullable=False)
    published_date = Column(DateTime, nullable=False, default=func.now())
    created_date = Column(DateTime, nullable=False, default=func.now())


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
Base = declarative_base()
db_url = 'postgresql://app_user:@pp_u53r@localhost:5432/test_db'
engine = create_engine(db_url, echo=True)
Base.metadata.create_all(engine)