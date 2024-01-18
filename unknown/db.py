from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import config

engine = create_engine(config.SQLALCHEMY_DATABASE_URI)

# scoped_session : 커넥션 풀과 유사, 
# 데이터 베이스 연결 세션을 여러개 생성하지 않고 생성된 세션을 사용하는 형식
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
# 모델 생성 기능 : Depts, User
de_ba = declarative_base()
de_ba.query = db_session.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import db_list  # 프로젝트에 필요한 모델 클래스
    de_ba.metadata.create_all(bind=engine)

