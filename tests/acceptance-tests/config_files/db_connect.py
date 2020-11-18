import psycopg2

from config_files import db_config


class DBConnect:

    def __init__(self):
        self._db_cur = self.db_connection()

    def db_connection(self):
        try:
            # Obtain the configuration parameters
            params = db_config.db_config_parameters()
            # Connect to the PostgreSQL database
            self._db_connection = psycopg2.connect(**params)
            # Establish a connection to the database by creating a cursor object
            return self._db_connection.cursor()
        except Exception as error:
            print(error)

    def db_select_query(self, query):
        result_records = []
        try:
            self._db_cur.execute(query)
            table_data = self._db_cur.fetchall()

            # iterate the list of tuple rows
            for row in table_data:
                for cell in row:
                    result_records.append(cell)
            return result_records
        except Exception as error:
            print("Error while fetching data from PostgreSQL", error)
        finally:
            # closing database connection
            self.db_close()

    def db_close(self):
        self._db_cur.close()
        self._db_connection.close()
