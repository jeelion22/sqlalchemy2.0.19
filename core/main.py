from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.orm import Session
from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import insert
from sqlalchemy import select, bindparam


engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)

metadata_obj = MetaData()

# this is how table is created when ORM declarative mode is not used
user_table = Table(
    "user_account",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("name", String(30)),
    Column("fullname", String),
)

# print(user_table.c.name)
# print(user_table.c.keys())
# print(user_table.primary_key)

address_table = Table(
    "address",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("user_id", ForeignKey("user_account.id"), nullable=False),
    Column("email_address", String, nullable=False),
)

# print(metadata_obj.create_all(engine))
metadata_obj.create_all(engine)


# Establishing declarative base
class Base(DeclarativeBase):
    pass


print(Base.registry)
print(Base.metadata)

# explicit declation of values in Insert.values()
# stmt = insert(user_table).values(name="Jeeva", fullname="Jeeva Madhaiyan")
# print(stmt)

# automatic representation of Values clause
stmt = insert(user_table)
print(stmt)

compiled = stmt.compile()
print(compiled.params)

with engine.connect() as conn:
    result = conn.execute(stmt)
    conn.commit()


# resturns column level default value if single row is inserted
print(result.inserted_primary_key)


with engine.connect() as conn:
    result = conn.execute(
        insert(user_table),
        [
            {"name": "Harry", "fullname": "Harry Karthik"},
            {"name": "Poorna", "fullname": "Poorna Shri"},
        ],
    )
    conn.commit()

scalar_subq = (
    select(user_table.c.id)
    .where(user_table.c.name == bindparam("username"))
    .scalar_subquery()
)

with engine.connect() as conn:
    result = conn.execute(
        insert(address_table).values(user_id=scalar_subq),
        [
            {"username": "Harry", "email_address": "harry@gmail.com"},
            {"username": "Poorna", "email_address": "poorna@gmail.com"},
        ],
    )
    conn.commit()
insert_stmt = insert(address_table).returning(
    address_table.c.id, address_table.c.email_address
)

print(insert_stmt)

select_stmt = select(user_table.c.id, user_table.c.name + "@aol.com")
insert_stmt = insert(address_table).from_select(
    ["user_id", "email_address"], select_stmt
)

print(insert_stmt.returning(address_table.c.id, address_table.c.email_address))
