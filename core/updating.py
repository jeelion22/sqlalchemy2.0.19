from tables import users_table
from connect import engine
from sqlalchemy import update

stmt = (
    update(users_table)
    .where(users_table.c.fullname == "Abinaya Madhaiyan")
    .values(email_id="abinayamadhaiyan.maths@gmail.com", name="Abinaya")
)

print(stmt)

with engine.connect() as conn:
    conn.execute(stmt)
    conn.commit()
