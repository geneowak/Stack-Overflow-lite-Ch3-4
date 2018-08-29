import psycopg2
from pprint import pprint
from .database_ini import development_db_config, test_db_config, db_tables, table_names


class DbHandler:
    def __init__(self):
        try:
            from API.app import app
            if app.config['TESTING']:
                self.conn = psycopg2.connect(**test_db_config)
                pprint("Using test db....")
            else:
                self.conn = psycopg2.connect(**development_db_config)
                pprint("Using development db....")
            self.conn.autocommit = True
            self.cursor = self.conn.cursor()

        except (Exception, psycopg2.DatabaseError) as error:
            pprint(error)

    def close_conn(self):
        self.cursor.close()
        self.conn.close()

    def create_tables(self):
        # create the db tables if they don't exit
        # pprint("Creating tables....")
        for table in db_tables():
            # pprint(table)
            self.cursor.execute(table)
        # pprint("Created tables....")

    def drop_all_tables(self):
        tb_names = table_names()
        for key in tb_names:
            self.cursor.execute("DROP TABLE {} CASCADE".format(tb_names[key]))
    

# if __name__ == '__main__':
#     dbHandle = DbHandler()
#     dbHandle.create_tables()
#     dbHandle.close_conn()
    
