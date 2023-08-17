from tables import users_table
from connect import engine
from sqlalchemy import delete

stmt = delete(users_table).where(users_table.c.name == "Jeeva")

with engine.connect() as conn:
    conn.execute(stmt)
    conn.commit()
