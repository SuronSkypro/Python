
from sqlalchemy import create_engine

DB_connection_string = "postgresql://postgres:postgres@Server1C:5432/SkyPro"
NEW_subject_ID = 0

def test_coonection_DB():
    Skypro_DB = create_engine(DB_connection_string)
    SkyproTables=Skypro_DB.table_names()
    assert SkyproTables[0] == 'users'

def test_insert_DB():
    global NEW_subject_ID

    Skypro_DB = create_engine(DB_connection_string)
    sql = "INSERT INTO subject (subject_title) VALUES('Тестировщик SkyPro') RETURNING subject_id"
    row = Skypro_DB.execute(sql)
    NEW_subject_ID = row.scalar()
    assert NEW_subject_ID > 0

def test_update_DB():
    global NEW_subject_ID

    Skypro_DB = create_engine(DB_connection_string)
    sql = "UPDATE subject SET subject_title='тестировщик SkyPro Исправлено' where subject_id="+str(NEW_subject_ID)
    row = Skypro_DB.execute(sql)

    sql = "select subject_title from subject where subject_id="+str(NEW_subject_ID)
    row = Skypro_DB.execute(sql)
    new_title = row.scalar()

    assert new_title == 'тестировщик SkyPro Исправлено'


def test_delete_DB():
    global NEW_subject_ID

    Skypro_DB = create_engine(DB_connection_string)
    sql = "DELETE from subject  where subject_id="+str(NEW_subject_ID)
    row = Skypro_DB.execute(sql)

    sql = "select subject_title from subject where subject_id="+str(NEW_subject_ID)
    row = Skypro_DB.execute(sql)
    assert row.rowcount == 0
