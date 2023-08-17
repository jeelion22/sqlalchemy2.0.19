from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import MetaData
from sqlalchemy import String, Integer
from sqlalchemy import ForeignKey


metadata_obj = MetaData()


"""
    user table
        - id pk
        - name str
        - fullname str
        -email

    comments tables
        - id pk
        - comment str
        user_id int > user.id
    
"""

users_table = Table(
    "users",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("fullname", String, nullable=False),
    Column("email_id", String, nullable=False),
)

comments_table = Table(
    "comments",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("comment", String, nullable=False),
    Column("user_id", ForeignKey("users.id"), nullable=False),
)
