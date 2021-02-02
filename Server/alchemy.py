import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

class User(object):
    def __init__(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password

    def __repr__(self):
        return "<User('%s','%s', '%s')>" % (self.name, self.fullname, self.password)

def main():
    metadata = MetaData()
    users_table = Table('users', metadata,
                        Column('id', Integer, primary_key=True),
                        Column('name', String),
                        Column('fullname', String),
                        Column('password', String)
                        )




    engine = create_engine('postgresql://postgres:root@localhost/mydatabase')
    # "Host=localhost;Database=site2;Username=postgres;Password=root"
    Base.metadata.create_all(engine)

if __name__ == '__main__':
    main()