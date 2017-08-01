from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
import datetime
import time

Base = declarative_base()


class Session(Base):
    __tablename__='session'
    id = Column(Integer, primary_key=True)
    type = Column(String(20), nullable=False)
    start = Column(DateTime, nullable=False)
    end = Column(DateTime, nullable=True)

engine = create_engine('sqlite:///timeme.db')
#Base.metadata.create_all(engine)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

#insert new session
#new_session = Session(type='studying', start=datetime.datetime.now())
#session.add(new_session)
#session.commit()

#record = session.query(Session).first()
#print(record.type, record.start)


class TimeTracker():
    
    def __init__(self, dbsession):
        self.__dbsession = dbsession

    def start(self, sessiontype):
        self.end()
        new_session = Session(type=sessiontype, start=datetime.datetime.now())
        self.__dbsession.add(new_session)
        self.__dbsession.commit()

    def end(self):
        last = self.__dbsession.query(Session).filter(Session.end==None).all()[-1]
        if last:
            last.end = datetime.datetime.now()
            self.__dbsession.add(last)
            self.__dbsession.commit()



def main():
    tt = TimeTracker(session)

    tt.start('Gaming')
    time.sleep(2)
    tt.start('Gaming')
    tt.end()

if __name__ == "__main__":
    main()

