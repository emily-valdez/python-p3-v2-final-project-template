from models.config import CURSOR, CONN

class Answer:
    all = {}
    def __init__(self, question_id, response, id = None): 
        self.question_id = question_id
        self.response = response
        self.id = id

    @classmethod
    def all(cls):
        sql = 'SELECT * FROM answers'
        list_of_tuples = CURSOR.execute(sql).fetchall()
        return [Answer.from_db(row) for row in list_of_tuples]

    @classmethod
    def from_db(cls, row_tuple):
        answer_instance = Answer(row_tuple[1], row_tuple[2])
        answer_instance.id = row_tuple[0]
        return answer_instance

    def delete(self):
        sql = 'DELETE FROM answers WHERE id = ?'
        # params_tuple = (self.id,)
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None

    def save(self):
        sql = ''' INSERT INTO answers (question_id, response)
        VALUES(?,?)
        '''
        CURSOR.execute(sql, (self.question_id, self.response))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    # @classmethod
    # def create_table(cls):
    #     sql = '''
    #         CREATE TABLE answers (
    #         id INTERGER PRIMARY KEY,
    #         question_id INTERGER,
    #         response TEXT
    #         )
    #     '''
    #     CURSOR.execute(sql)

    @classmethod
    def create(cls, question_id, response):
        new_answer = cls(question_id, response)
        new_answer.save()
        return new_answer

    @classmethod
    def find_by_id(cls, id ):
        sql = 'SELECT * FROM answers WHERE id = ?'
        row = CURSOR.execute(sql, (id,)).fetchone()
        return Answer.from_db(row) if row else None
     
        


    
        