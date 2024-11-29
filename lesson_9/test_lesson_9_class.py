from sqlalchemy import create_engine

DB_connection_string = "postgresql://postgres:postgres@Server1C:5432/SkyPro"
NEW_subject_ID =0 


class SkyProDB:
    def __init__(self, connection_string):
        self.engine = create_engine(connection_string)
        
    def test_connection(self):
        SkyproTables=self.engine.table_names()
        return SkyproTables[0]
        
        
        
    def insert_subject(self):
        global NEW_subject_ID
        sql = "INSERT INTO subject (subject_title) VALUES('Тестировщик SkyPro') RETURNING subject_id"
        row = self.engine.execute(sql)
        NEW_subject_ID =  row.scalar()
        return NEW_subject_ID
            

    
    def update_subject(self):
        global NEW_subject_ID
        
        sql = "UPDATE subject SET subject_title='тестировщик SkyPro Исправлено' where subject_id="+str(NEW_subject_ID)
        row = self.engine.execute(sql)

        sql = "select subject_title from subject where subject_id="+str(NEW_subject_ID)
        row = self.engine.execute(sql)
        new_title = row.scalar()    
        return new_title

        

        
        
    
    def delete_subject(self):
        global NEW_subject_ID

        sql = "DELETE from subject  where subject_id="+str(NEW_subject_ID)
        row = self.engine.execute(sql)

        sql = "select subject_title from subject where subject_id="+str(NEW_subject_ID)
        row = self.engine.execute(sql)
        return row.rowcount

def test_connection():
    db_tester = SkyProDB(DB_connection_string)
    assert db_tester.test_connection() == 'users'


def test_insert():
    db_tester = SkyProDB(DB_connection_string)
    assert db_tester.insert_subject()  > 0



def test_update():
    db_tester = SkyProDB(DB_connection_string)
    tempSUB = db_tester.update_subject()

    assert tempSUB  == 'тестировщик SkyPro Исправлено'


def test_delete():
    db_tester = SkyProDB(DB_connection_string)
    assert db_tester.delete_subject() == 0
