from core.model import meta
from sqlalchemy import create_engine
import sqlalchemy
import os
from dotenv import load_dotenv

load_dotenv()

#import session for database interaction
from sqlalchemy.orm import sessionmaker

def create_db():
    # define Base class for table class inheritance
    try:
        # create a DB engine connection
        engine = create_engine(os.getenv('DB_ENGINE'))
        
        # create table on table
        meta.create_all(engine)
        
        # create a session variable and bind the engine to it
        Session = sessionmaker(bind=engine)
        
        # instatiate the session
        session = Session()
        
        return session
    
    except AttributeError as e:
        print(f'error message {e}')
        
    except sqlalchemy.exc.ProgrammingError as e:
        print(f'An Error occured: {e}')

# call the session method
session = create_db()