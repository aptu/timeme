from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
import datetime
import time
import os

Base = declarative_base()


class Session(Base):
    __tablename__='session'
    id = Column(Integer, primary_key=True)
    type = Column(String(20), nullable=False)
    start = Column(Integer, nullable=False)
    end = Column(Integer, nullable=True)

#create an engine that stores data in local directory
dbpath = 'timeme.db'
engine = create_engine('sqlite:///' + dbpath)


#Bind engine and session
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
        #create all tables
        if not os.path.exists(dbpath):
            Base.metadata.create_all(engine)
            
    def deletedb(self):
        os.remove(dbpath)
                

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
        result = {}
                   
            
         # find the timestamp for 1st day of using the program to coumt total days
        day1 = session.query(func.min(Session.start).label('work')).one()[0] 
        try:
            total_days = round((datetime.datetime.now().timestamp() - day1) / 86400)
            total_work = [ item for item in alldata if item[0] == 'work' ][0]
            total_work = round(total_work[1] / 3600)
            total_relax = [ item for item in alldata if item[0] == 'relax' ][0]
            total_relax = round(total_relax[1] / 3600)
            avg_work = total_work / total_days
        except TypeError:
            total_days = 0
            total_work = 0
            total_relax = 0
            avg_work = 0.0
        
        #total time spent for work in hours  
        result['total_w'] = str(total_work)
        result['avg_w'] = round(avg_work, 1)
        
        #total time spent for relaxing in hours       
        result['total_r'] = str(total_relax)
        result['days'] = str(total_days)       
          
                             
        #print("===========")
        #for i in alldata:
         #   print("%.2f" % i[1])
        return result
 
