import psycopg2
from pprint import pprint
# from API.app import app
import API.app
from database_ini import development_db_config, test_db_config, db_tables, table_names


class DbHandler:
    def __init__(self):
        try:
            if app.config['TESTING']:
                self.conn = psycopg2.connect(**test_db_config)
            else:
                self.conn = psycopg2.connect(**development_db_config)
            self.conn.autocommit = True
            self.cursor = self.conn.cursor()

            # create the db tables if they don't exit
            for table in db_tables():
                self.cursor.execute(table)

        except (Exception, psycopg2.DatabaseError) as error:
            pprint(error)

    def close_conn(self):
        self.cursor.close()
        self.conn.close()

    def drop_all_tables(self):
        tb_names = table_names()
        for key in tb_names:
            self.cursor.execute("DROP TABLE {} CASCADE".format(tb_names[key]))
    

# if __name__ == '__main__':
#     db = DbHandler()
#     db.drop_all_tables()
