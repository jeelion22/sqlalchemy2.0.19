from main import session
from models import User, Comment
from sqlalchemy import Select

# stmt = Select(User).where(User.username.in_(["Jeeva", "Harry"]))

# result = session.scalars(stmt)

# for user in result:
#     print(user)

users = session.query(User).all()

for user in users:
    print(user)
