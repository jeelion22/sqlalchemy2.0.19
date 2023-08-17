from sqlalchemy import create_engine
from sqlalchemy import text

engine = create_engine("sqlite:///sample.db", echo=True)

with engine.connect() as conn:
    result = conn.execute(text("SELECT 'HELLO'"))
    print(result.all())
