from sqlalchemy import create_engine, MetaData, Table, func
from sqlalchemy.orm import sessionmaker

import datetime
import Addlayout
from DB import Customer

engine = create_engine('sqlite:///test2.db', echo=False)
metadata = MetaData(engine)
Session = sessionmaker(bind=engine)
session = Session()
# for each_customer in session.query(Customer):
#     print(each_customer.id)
ts = datetime.datetime.utcnow()
objects = [
    Customer(id="customeralice4321",company_name="Courier Corp.",title="mr",contact_name="alice bob", first_name="alice",last_name="bob",market_group="Auckland",
             address_one="St. BOB, Port Hank, Auckland",address_two="New Zealand", phone_number_one="323", phone_number_two="678334",
             city="Auckland", post_code="0116"),
    Customer(id="customercat224211", company_name="Hawk Corp.", title="mrs",contact_name="alice hawk", first_name="alice", last_name="hawk",
             market_group="Auckland",
             address_one="St. Luis, Port Kuku, Auckland", address_two="New Zealand", phone_number_one="323",
             phone_number_two="564566",
             city="Auckland", post_code="0156"),
    Customer(id="customerdog44631",company_name="Chicken Corp.",title="ms",contact_name="dog bob",first_name="dog",last_name="bob",market_group="Auckland",
             address_one="St. BOB, Port Hank, BOB city",address_two="New Zealand", phone_number_one="323", phone_number_two="5466534",
             city="Auckland", post_code="0126"),
]

# session.bulk_save_objects(objects)
# customer_table = Table('customer', metadata, autoload=True)
# for c in customer_table.c:
#     print(c.name, c.type)

# print(func.now())
# for each_customer in session.query(Customer):
#     print(each_customer.create_date)
from sqlalchemy import or_
print(len(session.query(Customer).filter(or_(Customer.address_one.like('%aucklan%'), Customer.city.like('%auck%')))))
session.commit()

# https://www.jianshu.com/p/196b7892cf38