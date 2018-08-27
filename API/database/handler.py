

def create_db_tables():
    create_user_tb = """CREATE TABLE IF NOT EXISTS users (
        id serial PRIMARY KEY,
        username VARCHAR (50) UNIQUE NOT NULL,
        password VARCHAR (100) NOT NULL,
        create_date TIMESTAMP NOT NULL,
        last_login TIMESTAMP
        )"""
    create_questions_tb = """CREATE TABLE IF NOT EXISTS (
        
        )"""
    create_answers_tb = """CREATE TABLE IF   NOT EXISTS (
        
        )"""
    create_comments_tb = """CREATE TABLE IF  NOT EXISTS (
        
        )"""