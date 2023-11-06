import sqlite3
# this connects us to the database
CONN = sqlite3.connect('holidays.db')
# this creates a tool where we can talk to the database
CURSOR = CONN.cursor()

class Questions:
    def __init__(self, question, id = None ):
        self.question = question
        self.id = id

    @classmethod
    def create_table(cls):
        sql = '''
            CREATE TABLE questions (
            id INTERGER PRIMARY KEY,
            question TEXT
            )
        '''
        CURSOR.execute(sql)

    @classmethod
    def delete_table(cls):
        sql = 'DELETE FROM questions'

        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def all(cls):
        sql = 'SELECT * FROM questions'

        list_of_tuples = CURSOR.execute( sql ).fetchall()
        return [cls.instance_from_db(row) for row in list_of_tuples]

    @classmethod
    def from_db(cls,row):
        question_instance = Questions( row[1],row[2] )
        question_instance.id = row[0]
        return question_instance
    
    @classmethod
    def find_by_id(cls,id):
        sql = '''
            SELECT * FROM questions WHERE id = ?
        '''

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
