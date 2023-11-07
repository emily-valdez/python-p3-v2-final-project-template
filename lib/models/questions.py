from models.config import CURSOR, CONN

class Question:
    def __init__(self, question, id = None ):
        self.question = question
        self.id = id

    def __repr__( self ):
        return f'{self.id}. {self.question}'

    @classmethod
    def all(cls):
        sql = 'SELECT * FROM questions'
        list_of_tuples = CURSOR.execute( sql ).fetchall()
        return [Question.from_db(row) for row in list_of_tuples]

    @classmethod
    def from_db(cls,row):
        question_instance = Question( row[1])
        question_instance.id = row[0]
        return question_instance
    
    def delete(self):
        sql = 'DELETE FROM questions WHERE id = ?'
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        self.id = None
    
    def save(self):
        sql = ''' INSERT INTO questions ( question )
        VALUES(?)
        '''
        CURSOR.execute(sql, ( self.question, ))
        CONN.commit()
        self.id = CURSOR.lastrowid

    @classmethod
    def create( cls, question ):
        new_question = cls( question )
        new_question.save()
        return new_question
    
    @classmethod
    def find_by_id(cls,id):
        sql = 'SELECT * FROM questions WHERE id = ?'
        row = CURSOR.execute(sql, (id,)).fetchone()
        return Question.from_db(row) if row else None
