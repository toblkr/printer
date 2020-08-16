from sqlalchemy import Column, String, create_engine, DateTime, TIMESTAMP ,text, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
import datetime

import win32ui

# 创建对象的基类:
Base = declarative_base()

db_link = 'sqlite:///Printer.db'

# 定义User对象:
class Customer(Base):
    # 表的名字:
    __tablename__ = 'customer'

    # 表的结构:
    # cid = Column(Integer,primary_key=True,autoincrement=True)
    id = Column(String(50), primary_key=True,index=True)
    batch = Column(String(50))
    company_name = Column(String(50))
    contact_name = Column(String(34))
    title = Column(String(5))
    other_title = Column(String(20))
    first_name = Column(String(20))
    last_name = Column(String(20))
    market_group = Column(String(50))
    address_one = Column(String(30))
    address_two = Column(String(30))
    address_three = Column(String(30))
    country = Column(String(30))
    # address_four = Column(String(50))
    phone_number_prefix = Column(String(10))
    phone_number = Column(String(30))
    fax_number_prefix = Column(String(10))
    fax_number = Column(String(30))
    city = Column(String(35))
    post_code = Column(String(10))
    # preferred_center = Column(String(50), ForeignKey("center.id"))
    # cost_center = Column(String(50), ForeignKey("center.id"))
    notes = Column(String(500))
    email_one = Column(String(50))
    email_two = Column(String(50))
    email_three = Column(String(50))
    create_date = Column(DateTime, default=datetime.date.today)
    update_date = Column(DateTime, default=datetime.date.today, onupdate=datetime.date.today)
    # city 和电话一行，公司名一行，联系人一行，地址三行，国家邮编一行共7行


    reserved_one = Column(String(100))
    reserved_two = Column(String(100))
    reserved_three = Column(String(100))
    reserved_four = Column(String(100))

    def __repr__(self):
        return self.id

class Sender(Base):
    # 表的名字:
    __tablename__ = 'sender'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    sender_name = Column(String(50))
    company_name = Column(String(50))
    address_one = Column(String(30))
    address_two = Column(String(30))
    address_three = Column(String(30))
    phone_number = Column(String(20))
    country = Column(String(30))

    city = Column(String(35))
    post_code = Column(String(10))

    reserved_one = Column(String(100))
    reserved_two = Column(String(100))
    reserved_three = Column(String(100))
    reserved_four = Column(String(100))

    create_date = Column(String(50))
    update_date = Column(String(50))

    def __repr__(self):
        return self.sender_name


class PrintSize(Base):
    # 表的名字:
    __tablename__ = 'print_size'

    # 表的结构:
    id = Column(Integer(), primary_key=True,autoincrement=True)
    tag_size = Column(String(4))
    last_use = Column(String(2))
    font_size = Column(Integer())
    line_space = Column(Integer())



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
    engine = create_engine(db_link,echo=False)
    font_80 = 12
    font_100 = 15
    y_100_distance = 62
    y_80_distance = 45

    if not engine.dialect.has_table(engine, 'center'):
        print('Database not exist')
        Base.metadata.create_all(engine)
        print('created')
    else:
        print('Database already there')
        try:
            Session = sessionmaker(bind=engine)
            session = Session()
            data = session.query(PrintSize).all()
            if(len(data)==0):
                Size_100 = PrintSize(tag_size='10',last_use='1',font_size=font_100,line_space=y_100_distance)
                Size_80 = PrintSize(tag_size='8', last_use='1', font_size=font_80,line_space=y_80_distance)
                session.add(Size_100)
                session.add(Size_80)
                session.commit()
            print(data[0].line_space)
        except Exception as e:
            PrintSize.__table__.drop(engine)
            Base.metadata.create_all(engine)
            Session = sessionmaker(bind=engine)
            session = Session()
            data = session.query(PrintSize).all()
            Size_100 = PrintSize(tag_size='10', last_use='1', font_size=font_100, line_space=y_100_distance)
            Size_80 = PrintSize(tag_size='8', last_use='1', font_size=font_80, line_space=y_80_distance)
            session.add(Size_100)
            session.add(Size_80)
            session.commit()
            print(data)


