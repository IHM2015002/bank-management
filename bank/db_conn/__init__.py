from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_url = 'mysql+pymysql://root:root@localhost/fastdb'


# connect_args={'charset':'utf8mb4'} is not required it is added for supporting more complex data in db to store like emoji
# support 4-byte char by default 3-byte char is supported
engine = create_engine(db_url, connect_args={'charset':'utf8mb4'})

Base = declarative_base()

SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

# Base.metadata.create_all(bind=engine)

