''' development database configurations '''
development_db_config = {
    'host':'localhost',
    "dbname": "stack_over_flow_app",
    "password": 'postgres',
    "user": "postgres",
}
''' test database configurations '''
test_db_config = {
    'host':'localhost',
    "dbname": "test_db",
    "password": 'postgres',
    "user": "postgres",
}
''' names of all the tables in the database '''
table_names = {
    "users": "users",
    "questions": "questions",
    "answers": "answers",
    "answer_comments": "answer_comments",
    "question_comments": "question_comments"
}


def db_tables():
    ''' returns a list all the queries needed to create the database tables '''
    create_user_tb = """CREATE TABLE IF NOT EXISTS {} (
        user_id serial PRIMARY KEY,
        username VARCHAR (50) UNIQUE NOT NULL,
        email VARCHAR (100) UNIQUE NOT NULL,
        password VARCHAR (100) NOT NULL,
        create_date TIMESTAMP NOT NULL,
        last_login TIMESTAMP DEFAULT NULL
        )""".format(table_names["users"])

    create_questions_tb = """CREATE TABLE IF NOT EXISTS {} (
        qn_id serial PRIMARY KEY,
        title VARCHAR (100) NOT NULL,
        description VARCHAR (255) NOT NULL,
        user_id INTEGER NOT NULL,
        create_date TIMESTAMP,
        FOREIGN KEY(user_id)
            REFERENCES users(user_id)
            ON DELETE CASCADE ON UPDATE CASCADE
        )""".format(table_names["questions"])

    create_answers_tb = """CREATE TABLE IF   NOT EXISTS {} (
        ans_id serial PRIMARY KEY,
        answer VARCHAR (255) NOT NULL,
        qn_id INTEGER NOT NULL,
        user_id INTEGER NOT NULL,
        preferred VARCHAR (10) DEFAULT 'false',
        create_date TIMESTAMP,
        FOREIGN KEY(qn_id)
            REFERENCES questions(qn_id)
            ON DELETE CASCADE ON UPDATE CASCADE,
        FOREIGN KEY(user_id)
            REFERENCES users(user_id)
            ON DELETE CASCADE ON UPDATE CASCADE
        )""".format(table_names["answers"])

    create_question_comments_tb = """CREATE TABLE IF  NOT EXISTS {} (
        id serial PRIMARY KEY,
        comment VARCHAR (255) NOT NULL,
        qn_id INTEGER NOT NULL,
        user_id INTEGER NOT NULL,
        create_date TIMESTAMP,
        FOREIGN KEY(qn_id)
            REFERENCES questions(qn_id)
            ON DELETE CASCADE ON UPDATE CASCADE,
        FOREIGN KEY(user_id)
            REFERENCES users(user_id)
            ON DELETE CASCADE ON UPDATE CASCADE
        )""".format(table_names["question_comments"])
        
    create_answer_comments_tb = """CREATE TABLE IF  NOT EXISTS {} (
        id serial PRIMARY KEY,
        comment VARCHAR (255) NOT NULL,
        ans_id INTEGER NOT NULL,
        user_id INTEGER NOT NULL,
        create_date TIMESTAMP,
        FOREIGN KEY(ans_id)
            REFERENCES answers(ans_id)
            ON DELETE CASCADE ON UPDATE CASCADE,
        FOREIGN KEY(user_id)
            REFERENCES users(user_id)
            ON DELETE CASCADE ON UPDATE CASCADE
        )""".format(table_names["answer_comments"])

    return [
        create_user_tb,
        create_questions_tb,
        create_answers_tb,
        create_answer_comments_tb,
        create_question_comments_tb
    ]

