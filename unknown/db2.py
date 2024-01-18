from sqlalchemy import create_engine, MetaData, Table
import config

engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
metadata = MetaData(bind=engine)

bread = Table('bread', metadata, autoload=True)
drink = Table('drink', metadata, autoload=True)
store = Table('store', metadata, autoload=True)
review = Table('review', metadata, autoload=True)



