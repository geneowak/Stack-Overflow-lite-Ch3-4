import os
import psycopg2
import psycopg2.extras
from pprint import pprint
from .database_ini import development_db_config, test_db_config, db_tables, table_names


class DbHandler:
    ''' 
    This class is the base database class that handles general actions on the database
    '''
    def __init__(self):
        ''' creates connection and a cursor objects '''
        try:
            from API.app import app
            if os.getenv('FLASK_ENV') == 'HEROKU11':
                self.conn = psycopg2.connect(os.getenv('DATABASE_URL'))
                # pprint("Using HEROKU db....")
            elif app.config['TESTING']:
                self.conn = psycopg2.connect(**test_db_config)
                # pprint("Using test db....")
            else:
                self.conn = psycopg2.connect(**development_db_config)
                # pprint("Using development db....")
            self.conn.autocommit = True
            self.cursor = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        except (Exception, psycopg2.DatabaseError) as error:
            raise error

    def close_conn(self):
        ''' closes the connection to the database '''
        self.cursor.close()
        self.conn.close()

    def create_tables(self):
        ''' creates the tables in the database if they don't exit '''
        # pprint("Creating tables....")
        for table in db_tables():
            # pprint(table)
            self.cursor.execute(table)
        # pprint("Created tables....")

    def drop_all_tables(self):
        ''' deletes all the tables in the database '''
        for key in table_names:
            self.cursor.execute("DROP TABLE IF EXISTS {} CASCADE".format(table_names[key]))
    

# if __name__ == '__main__':
#     dbHandle = DbHandler()
#     dbHandle.create_tables()
#     dbHandle.close_conn()
    
