
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.model import Model, Base
from models.user import User
from models.post import Post


class Db:
    """ database class """

    session = None
    __engine = None
    __db_host = "localhost"
    __db_name = "blog"
    __username = "root"
    __pass = "nana"

    def __init__(self):
        self.__engine = create_engine(f"""mysql+pymysql://{self.__username}:{self.__pass}@{self.__db_host}/{self.__db_name}""", echo=False)
        Session = sessionmaker(bind=self.__engine)
        Base.metadata.create_all(self.__engine)
        self.session = Session()
    