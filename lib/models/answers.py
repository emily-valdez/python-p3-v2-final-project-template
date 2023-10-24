import sqlite3
connection = sqlite3.connect('holidays.db')
cursor = connection.cursor()

class Answer:
    def __init__(self, name, question_id, response, id = None):
        self.name = name
        self.question.id = question.id
        self.response = response
        self.id = id

    

    @classmethod
    def all(cls):
        sql = 'SELECT * FROM answers'
        list_of_tuples = cursor.execute(sql).fetchall()
        return [Answer.from_db(row) for row in list_of_tuples]

    @classmethod
    def from_db(cls, row_tuple):
        answer_instance = Answer(row_tuple[1], row_tuple[2], row_tuple[3])
        answer_instance.id = row_tuple[0]
        return answer_instance

    @classmethod
    def delete_table(cls):
        sql = 'DELETE FROM answers'
        cursor.execute(sql)
        connection.commit()

    @classmethod
    def create_table(cls):
        sql = '''
            CREATE TABLE answers(
                id INTEGER PRIMARY KEY,
                name TEXT,
                question_id INTEGER,
                response TEXT
            )
        '''
        cursor.execute(sql)

    def delete(self):
        sql = 'DELETE FROM answers WHERE id = ?'
        params_tuple = (self.id,)
        cursor.execute(sql, params_tuple)
        connection.commit()
        self.id = None

    @classmethod
    def create(cls, name, question_id, response):
        new_answer = cls(name, question_id, response):
        sql = 'INSERT INTO answers (name, question_id, response) VALUES(?, ?, ?)'
        params_tuple = (new_answer.name, new_answer.question_id, new_answer.response)
        cursor.execute(sql, params_tuple)
        connection.commit()
        return new_answer

    @classmethod
    def find_by_id(cls):
        sql = 'SELECT * FROM answers WHERE id = ?'
        row = cursor.execute(sql, (id,)).fetchone()
        return Answer.from_db(row) if row else None
     
        


    
        