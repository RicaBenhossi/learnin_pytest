from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DbConnection():
    def __init__(self):
        self.__engine = create_engine('mysql+pymysql://root:bruce@127.0.0.1:3306/seguros')
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()

    def __get_connection(self):
        return self.__engine.connect()

    def get_session(self):
        return self.__session

    def get_cursor(self):
        return self.__engine.cursor(buffered=True, dictionary=True)
