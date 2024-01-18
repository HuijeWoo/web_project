from db import init_db, db_session, engine
from db_list import Bread, Drink, Store, Review
from sqlalchemy import select, delete, insert, update


if __name__ == '__main__' : 
    # 데이터베이스 테이블 생성
    init_db()
    print('>>>>>>>>>>>>>>>>>>>>>>>>')
    # 데이터 입력
    # u = User('son', 'son@localhost')
    # db_session.add(u)

    # d = Dept(10, '개발팀', '서울')
    # db_session.add(d)
    # db_session.commit()

    # 데이터 추출 (select)
    # print(type(User.query.all()), User.query.all())
    # print(type(Dept.query.all()), Dept.query.all())

    # for dept in Dept.query.all() :
    #     print(type(dept), dept, dept.dname)

    # print('-------------------------------------')
    # print(Dept.query.first())

    # stmt1 = select(User).where(User.name == 'son')
    # print(stmt1)
    # with engine.connect() as conn:
    #     for row in conn.execute(stmt1):
    #         print(row)

    # ####################################################
    # 참고
    # https://soogoonsoogoonpythonists.github.io/sqlalchemy-for-pythonist/tutorial/5.1.%20Core%EC%99%80%20ORM%20%EB%B0%A9%EC%8B%9D%EC%9C%BC%EB%A1%9C%20%ED%96%89%20%EC%A1%B0%ED%9A%8C%ED%95%98%EA%B8%B0.html


