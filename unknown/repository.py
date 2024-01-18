from db import engine, db_session
from db_list import Bread, Drink, Store, Review
from sqlalchemy import select, delete, insert, update, text
import random

conn = db_session.connection()

# Depts 테이블의 CRUD


    # global conn
    
    # sql1 = select(Dept)
    # sql1 = select(Dept).where(Dept.deptno == deptno)
    # sql1 = insert(Dept).values(dname=dname, loc=loc)
    # sql1 = update(Dept).where(Dept.deptno == deptno).values(dname=dname, loc=loc)
    # sql1 = delete(Dept).where(Dept.deptno == deptno)
    
    # print('conn >>>>>>>> ', conn)
    # result1 = conn.execute(sql1)
    # result_list1 = list(result1)
    # print(result_list1)
    
    # update, insert, delete는 commit 필수.
    # conn.commit()

def InsertBread():
    name_candidates = ['식빵', '사과파이', '커피번', '소보루빵', '바게트빵']
    #price 1500 ~ 5000원 100단위
    #weight 100 ~ 200g 10단위
    #total_cal 100~300kcal 10 단위
    #store_id s0001~s0100
    
    for i in range(100):
        sql1 = insert(Bread).values(
            bread_id= 'b' + str(i).zfill(4),
            name=random.choice(name_candidates) + str(i),
            price=random.randrange(1500, 5000, 100),
            weight=random.randrange(100, 200, 10),
            total_cal=random.randrange(100, 300, 10),
            store_id = 's' + str(random.randint(1,100)).zfill(4)
        )
        conn.execute(sql1)
        
    conn.commit()
    

def InsertDrink():
    global conn
    name_candidates = ['orange_juice', 'milk', 'coffee', 'tea', 'cocoa']
    #price 1500 ~ 5000원 100단위
    #volume 250 ~ 500mL 50단위
    #total_cal 10~200kcal 10 단위
    #store_id s0001~s0100
    
    for i in range(100):
        sql1 = insert(Drink).values(
            drink_id= 'd' + str(i).zfill(4),
            name=random.choice(name_candidates) + str(i),
            price=random.randrange(1500, 5000, 100),
            volume=random.randrange(250, 500, 50),
            total_cal=random.randrange(10, 200, 10),
            store_id = 's' + str(random.randint(1,100)).zfill(4)
        )
        conn.execute(sql1)
        
    conn.commit()
    
def InsertStore():
    global conn
    
    
def InsertReview():
    global conn
    

if __name__ == '__main__':
    #InsertBread()
    #InsertDrink()
    pass