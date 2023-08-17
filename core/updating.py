from tables import users_table
from connect import engine
from sqlalchemy import update

stmt = (
    update(users_table)
    .where(users_table.c.fullname == "Abinaya Madhaiyan")
    .values(fullname="jeemad", name="jeeva")
)

print(stmt)

with engine.connect() as conn:
    conn.execute(stmt)
    conn.commit()
