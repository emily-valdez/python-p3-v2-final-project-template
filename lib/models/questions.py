from __init__ import CURSOR, CONN

class Question:
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
    def create( cls, question, id = None ):
        new_question = cls(question, id = None)
        sql = 'INSERT INTO answers (question, id = None) VALUES(?, ?, ?)'
        params_tuple = (new_question.question, new_question.id)
        CURSOR.execute(sql, params_tuple)
        CONN.commit()
        return new_question

    @classmethod
    def delete_table(cls):
        sql = 'DELETE FROM questions'

        CURSOR.execute(sql)
        CONN.commit()

    def delete(self):
        sql = 'DELETE FROM question WHERE id = ?'
        params_tuple = (self.id,)
        CURSOR.execute(sql, params_tuple)
        CONN.commit()
        self.id = None

    @classmethod
    def all(cls):
        sql = 'SELECT * FROM questions'

        list_of_tuples = CURSOR.execute( sql ).fetchall()
        return [cls.from_db(row) for row in list_of_tuples]

    @classmethod
    def from_db(cls,row):
        question_instance = Question( row[1],row[2] )
        question_instance.id = row[0]
        return question_instance
    
    @classmethod
    def find_by_id(cls,id):
        sql = '''
            SELECT * FROM questions WHERE id = ?
        '''

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
