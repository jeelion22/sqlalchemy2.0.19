from tables import users_table
from connect import engine
from sqlalchemy import select


# stmt = select(users_table)

# print(stmt)

# with engine.connect() as conn:
#     result = conn.execute(stmt)

#     for row in result:
#         print(row)

# selecting row by certain condition

stmt = select(users_table).where(users_table.c.name != "Abinaya")
# stmt = select(users_table)

with engine.connect() as conn:
    result = conn.execute(stmt)

    print("id", "\t\tname", "\t\tfullname", "\t\temail_id")
    for row in result:
        print(row)
