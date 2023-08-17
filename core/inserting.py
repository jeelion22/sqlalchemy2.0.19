from sqlalchemy import insert
from tables import users_table
from connect import engine

# stmt = insert(users_table).values(
#     name="Jeeva", fullname="Jeeva Madhaiyan", email_id="jeelion22@gmail.com"
# )


# for multiple insert

stmt = insert(users_table)

# with engine.connect() as conn:
#     conn.execute(
#         stmt,
#         [
#             {
#                 "name": "Harry",
#                 "fullname": "Harry Karthik",
#                 "email_id": "harrykarthik.01@gmail.com",
#             },
#             {
#                 "name": "Abinaya",
#                 "fullname": "Abinaya Madhaiyan",
#                 "email_id": "abinayamadthaiyan@gmail.com",
#             },
#         ],
#     )
#     conn.commit()


with engine.connect() as conn:
    conn.execute(
        stmt,
        {
            "name": "Arun",
            "fullname": "Arun Madhaiyan",
            "email_id": "arunmadhaiyan.ic@gmail.com",
        },
    )
    conn.commit()
