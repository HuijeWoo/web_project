from sqlalchemy import create_engine, MetaData, Table
import config

engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
metadata = MetaData(bind=engine)

users = Table('users', metadata, autoload=True)
depts = Table('depts', metadata, autoload=True)



