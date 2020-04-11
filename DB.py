from sqlalchemy import Column, String, create_engine, DateTime, TIMESTAMP ,text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
import datetime

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class Customer(Base):
    # 表的名字:
    __tablename__ = 'customer'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    company_name = Column(String(50))
    contact_name = Column(String(50))
    title = Column(String(5))
    first_name = Column(String(50))
    last_name = Column(String(50))
    market_group = Column(String(50))
    address_one = Column(String(50))
    address_two = Column(String(50))
    address_three = Column(String(50))
    # address_four = Column(String(50))
    phone_number_one = Column(String(10))
    phone_number_two = Column(String(20))
    fax_number_one = Column(String(10))
    fax_number_two = Column(String(20))
    city = Column(String(100))
    post_code = Column(String(10))
    # preferred_center = Column(String(50), ForeignKey("center.id"))
    # cost_center = Column(String(50), ForeignKey("center.id"))
    notes = Column(String(500))
    email_one = Column(String(50))
    email_two = Column(String(50))
    email_three = Column(String(50))
    create_date = Column(TIMESTAMP,default=datetime.datetime.now)
    update_date = Column(TIMESTAMP,onupdate=datetime.datetime.now)
    # city 和邮编一行，公司名一行，联系人一行，地址三行，国家一行

    def __repr__(self):
        return self.id

class Sender(Base):
    # 表的名字:
    __tablename__ = 'sender'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    sender_name = Column(String(50))
    company_name = Column(String(50))
    address_one = Column(String(50))
    address_two = Column(String(50))
    address_three = Column(String(50))
    address_four = Column(String(50))
    phone_number_one = Column(String(10))

    city = Column(String(100))
    post_code = Column(String(10))

    create_date = Column(String(50))
    update_date = Column(String(50))

    def __repr__(self):
        return self.sender_name


class PrintSize(Base):
    # 表的名字:
    __tablename__ = 'print_size'

    # 表的结构:
    id = Column(String(20), primary_key=True)


class Center(Base):
    # 表的名字:
    __tablename__ = 'center'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    address = Column(String(30))

    def __repr__(self):
        return self.id

# 初始化数据库连接:



def init_db():
    engine = create_engine('sqlite:///test2.db',echo=False)
    if not engine.dialect.has_table(engine, 'center'):
        print('not exist')
        Base.metadata.create_all(engine)
        print('created')
    else:
        print('exist')

