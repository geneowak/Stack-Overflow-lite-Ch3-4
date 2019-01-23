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
                # create database table if it doesn't exist
                self.create_database(test_db_config)
                self.conn = psycopg2.connect(**test_db_config)
                # pprint("Using test db....")
            else:
                # create database table if it doesn't exist
                self.create_database(development_db_config)
                self.conn = psycopg2.connect(**development_db_config)
                # pprint("Using development db....")
            self.conn.autocommit = True
            self.cursor = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        except (Exception, psycopg2.DatabaseError) as error:
            pprint("an error occured...")
            pprint(error)
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

    def create_database(self, dbconfig):
        ''' creates a database if it doesn't exist '''

        try:
            dbname = dbconfig["dbname"]
            paswd = dbconfig["password"]
            user = dbconfig["user"]
            host = dbconfig["host"]

            # make a connection
            conn = psycopg2.connect(dbname="postgres", user=user, host=host, password=paswd)

            conn.autocommit = True
            # get a cursor
            cursor = conn.cursor()            
            
            get_db_query = "SELECT datname FROM pg_catalog.pg_database WHERE datname = '{}';".format(dbname)

            cursor.execute(get_db_query)
            # get result
            exists = cursor.fetchone()
            # pprint("....Printing result...")
            # pprint(exists)
            if not exists:
                pprint("Creating tables....")
                cursor.execute("CREATE DATABASE {}".format(dbname))

            # close the connection
            cursor.close()
            conn.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print("and error occured", error)
            raise error
            


        
    

# if __name__ == '__main__':
#     dbHandle = DbHandler()
#     dbHandle.create_tables()
#     dbHandle.close_conn()
    
