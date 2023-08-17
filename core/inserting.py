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
#                 "name": "Steve",
#                 "fullname": "Jobs",
#                 "email_id": "stevejobs@gmail.com",
#             },
#             {
#                 "name": "Steve",
#                 "fullname": "Steve Smith",
#                 "email_id": "stevesmith@email.com",
#             },
#         ],
#     )
#     conn.commit()


with engine.connect() as conn:
    conn.execute(
        stmt,
        {
            "name": "Arun",
            "fullname": "Arun Mad",
            "email_id": "arunmad@xyc.com",
        },
    )
    conn.commit()
