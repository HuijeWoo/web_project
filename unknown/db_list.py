# https://docs.sqlalchemy.org/en/20/core/constraints.html

from sqlalchemy import Column, CheckConstraint, Integer, String, Time, Day
from db import de_ba

class Bread(de_ba):
    __tablename__ = 'bread'
    # ex> b0001
    bread_id = Column(String(5), primary_key=True)
    name = Column(String(50), nullable=False)
    price = Column(Integer, nullable=False) # unit : won
    weight = Column(Integer, nullable=False) # unit : g (mass...)
    total_cal = Column(Integer, nullable=False) # unit : kcal
    store_id = Column(String(5)) # 판매하고 있는 매장 id

    def __init__(self, name=None, price=None, weight=None, total_cal=None, store_id=None):
        self.name = name
        self.price = price
        self.weight = weight
        self.total_cal = total_cal
        self.store_id = store_id
        
    def __repr__(self):
        return f'<Bread {self.name}>'
    
    def __str__(self) :
        return f'bread_id: {self.bread_id},\nname: {self.name},\nprice: {self.price}\nweight: {self.weight},\ntotal_cal: {self.total_cal}'

class Drink(de_ba):
    __tablename__ = 'drink'
    # ex> d0001
    drink_id = Column(String(5), primary_key=True)
    name = Column(String(50), nullable=False)
    price = Column(Integer, nullable=False) # unit : won
    volume = Column(Integer, nullable=False) # unit : mL
    total_cal = Column(Integer, nullable=False) # unit : kcal
    store_id = Column(String(5))
    
    def __init__(self, name=None, price=None, volume=None, total_cal=None, store_id=None):
        self.name = name
        self.price = price
        self.volume = volume
        self.total_cal = total_cal    
        self.store_id = store_id
        
    def __repr__(self):
        return f'<Drink {self.name}>'
    
    def __str__(self) :
        return f'drink_id: {self.drink_id},\nname: {self.name},\nprice: {self.price}\nvolume: {self.volume},\ntotal_cal: {self.total_cal}'
    

class store(de_ba):
    # ex> s00001
    store_id = Column(String(5), primary_key=True)
    name = Column(String(50), nullable=False)
    loc = Column(String(100), nullable=False) # ~~시 까지만.
    tel = Column(String(12), nullable=False) # no dash, only number
    open_time = Column(Time())
    close_time = Column(Time())
    
    def __init__(self, name=None, loc=None, tel=None, open_time=None, close_time=None):
        self.name = name
        self.loc = loc
        self.tel = tel
        self.open_time = open_time    
        self.close_time = close_time
    
    def __repr__(self):
        return f'<Store {self.name}>'
    
    def __str__(self) :
        return f'store_id: {self.store_id},\nname: {self.name},\nloc: {self.loc}\ntel: {self.tel},\nopen_time: {self.open_time},\nclose_time: {self.close_time}'
    

class review(de_ba):
    # ex> r00001
    review_id = Column(String(5), primary_key=True)
    store_id = Column(String(5), nullable=False)
    star = Column(Integer, CheckConstraint("star BETWEEN 1 AND 5"), nullable=False)
    comment = Column(String(100))
    
    def __init__(self, store_id=None, star=None, comment=None):
        self.store_id = store_id
        self.star = star
        self.comment = comment
        
    def __repr__(self):
        return f'<{self.store_id}\'s Review - {self.review_id}>'
    
    def __str__(self) :
        return f'review_id: {self.review_id},\nstore_id: {self.store_id},\nstar: {self.star}\ncomment: {self.comment}'
    
    
    