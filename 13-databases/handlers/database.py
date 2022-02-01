from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.models import User

engine = create_engine('mysql+mysqldb://root:root@localhost:3306/newdb')
Session = sessionmaker(engine)


def get_user_list():
    with Session() as session:
        user_list = session.query(User).all()

        return user_list


def create_user(first_name, last_name, email):
    with Session() as session:
        user = User(first_name=first_name, last_name=last_name, email=email)
        session.add(user)
        session.commit()

