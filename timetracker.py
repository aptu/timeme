from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, func
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
    start = Column(Integer, nullable=False)
    end = Column(Integer, nullable=True)

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
    
    def __init__(self):
        self.__dbsession = session

    def start(self, sessiontype):
        self.end()
        new_session = Session(type=sessiontype, start=datetime.datetime.now().timestamp())
        self.__dbsession.add(new_session)
        self.__dbsession.commit()

    def end(self):
        unclosed = self.__dbsession.query(Session).filter(Session.end==None).all()
        if len(unclosed) > 0:
            last = unclosed[-1]
            last.end = datetime.datetime.now().timestamp()
            self.__dbsession.add(last)
            self.__dbsession.commit()
    
    def stats(al=True, week=True, day=True):
        alldata = session.query(Session.type, func.sum(Session.end - Session.start)).filter(Session.end!=None).group_by(Session.type).all()
        #alldata = session.query(Session.type, Session.start, Session.end).filter(Session.end!=None).all()
        #alldata = session.query(func.count(Session.end)).all()
        #print(alldata)
        print("===========")
        for i in alldata:
            print("%.2f" % i[1])
        
        #if all:
            



#def main():
#    tt = TimeTracker(session)
#
#    tt.start('Gaming')
#    time.sleep(2)
#    tt.start('Gaming')
#    tt.end()
#
#if __name__ == "__main__":
#    main()
#