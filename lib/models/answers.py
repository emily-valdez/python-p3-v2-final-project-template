from models.config import CURSOR, CONN

class Answer:
    def __init__(self, question_id, response, id = None): 
        self.question_id = question_id
        self.response = response
        self.id = id

    

    def __repr__( self ):
        return f'{self.id}. {self.response}'

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
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        self.id = None

    def save(self):
        sql = ''' INSERT INTO answers (question_id, response)
        VALUES(?,?)
        '''
        CURSOR.execute(sql, (self.question_id, self.response))
        CONN.commit()
        self.id = CURSOR.lastrowid
        

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
    
    @classmethod
    def find_related_questions(cls, response):
        from models.questions import Question
        sql = 'SELECT question_id FROM answers WHERE response = ?'
        row = CURSOR.execute(sql, (response,)).fetchone()
        if row:
            question_id = row[0]
            associated_question = Question.find_by_id(question_id)
            if associated_question:
                return associated_question
        return None
    
    @property
    def question_id(self):
        return self._question_id

    @question_id.setter
    def question_id(self, question_id):
        if isinstance(question_id, int):
            self._question_id = question_id
        else:
            raise ValueError('question_id must be number')
        
    @property
    def response(self):
        return self._response

    @response.setter
    def response(self, response):
        if isinstance(response, str) and len(response) > 0:
            self._response = response
        else:
            raise ValueError('response must be non-empty string')
     
        


    
        