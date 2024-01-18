from db import engine, db_session
from deptModel import Dept, User
from sqlalchemy import select, delete, insert, update, text

conn = db_session.connection()

# Depts 테이블의 CRUD

# select All
def selectDeptsAll() :

    global conn

    sql1 = select(Dept)
    print(sql1)
    sql2 = '''SELECT depts.deptno, depts.dname, depts.loc 
              FROM depts'''
    print(sql2)


 
    print('conn >>>>>>>> ', conn)

    result1 = conn.execute(sql1)
    result2 = conn.execute(text(sql2))

    print(result1)
    print(result2)

    result_list1 = list(result1)
    result_list2 = list(result2)
    print(result_list1)
    print(result_list2)

# select by dptno
def selectDeptsbyDeptno(deptno) :

    global conn

    sql1 = select(Dept).where(Dept.deptno == deptno)
    print(sql1)
    sql2 = f'''SELECT depts.deptno, depts.dname, depts.loc 
            FROM depts 
            WHERE depts.deptno = {deptno}'''
    print(sql2)

    
    print('conn >>>>>>>> ', conn)

    result1 = conn.execute(sql1)
    result2 = conn.execute(text(sql2))

    print(result1)
    print(result2)

    result_list1 = result1.first()
    result_list2 = result2.first()
    print(type(result_list1) , result_list1)
    print(type(result_list2), result_list2)

# insert Dept
def insertDept(dname, loc):

    global conn

    sql1 = insert(Dept).values(dname=dname, loc=loc)
    print(sql1)
    sql2 = f'''INSERT INTO depts (dname, loc) VALUES (\'{dname}\', \'{loc}\')'''
    print(sql2)

    result1 = conn.execute(sql1)
    #result2 = conn.execute(text(sql2))

    # 입력 완료 : 물리적 처리
    conn.commit()
    
    print(result1.inserted_primary_key)
    #print(result2.inserted_primary_key)

# update Dept
def updateDept(deptno, dname, loc) :
    global conn

    sql1 = update(Dept).where(Dept.deptno == deptno).values(dname=dname, loc=loc)
    print(sql1)

    result1 = conn.execute(sql1)

    conn.commit()

    print(result1.rowcount)

# delete Dept
def deleteDept(deptno) :
    global conn

    sql1 = delete(Dept).where(Dept.deptno == deptno)
    print(sql1)

    result1 = conn.execute(sql1)

    conn.commit()

    print(result1.rowcount)

if __name__ == '__main__':
    #selectDeptsAll()
    #selectDeptsbyDeptno(10)
    #insertDept('개발팀', '서울')
    #updateDept(10, 'QA', '판교')
    deleteDept(13)


