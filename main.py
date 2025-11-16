from sqlalchemy.orm import Session  
from menu_definition import add_menu, list_menu, menu_main
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from db_connection import engine, Session


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from orm_base import Base

import models
import functions

SessionLocal = sessionmaker(bind=engine)

Base.metadata.create_all(engine)

def list_objects(sess: Session):
    list_action: str = ''
    while list_action != list_menu.last_action():
        list_action = list_menu.menu_prompt()
        exec(list_action)

def add_objects(sess: Session):
    add_action: str = ''
    while add_action != add_menu.last_action():
        add_action = add_menu.menu_prompt()
        exec(add_action)

def main():
    sess = SessionLocal()
    main_action = ''
    while main_action != menu_main.last_action():
        main_action = menu_main.menu_prompt()
        exec(main_action)
    # sess.commit()
if __name__ == "__main__":
    main()




        