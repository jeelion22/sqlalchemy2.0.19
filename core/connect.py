from sqlalchemy import create_engine

# from sqlalchemy import Table, String, Integer, Column
# from sqlalchemy import MetaData
from sqlalchemy import text

# metadata_obj = MetaData()

url = "sqlite:///sample.db"

engine = create_engine(url, echo=True)

# with engine.connect() as conn:
#     result = conn.execute(text("SELECT 'hello world'"))
#     print(result.all())
