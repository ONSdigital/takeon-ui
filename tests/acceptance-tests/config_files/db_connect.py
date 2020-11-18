import psycopg2

from config_files import db_config


class DBConnect:

    def __init__(self):
        try:
            # Obtain the configuration parameters
            params = db_config.db_config()
            # Connect to the PostgreSQL database
            self._db_connection = psycopg2.connect(**params)
            # Establish a connection to the database by creating a cursor object
            self._db_cur = self._db_connection.cursor()
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

    def db_close(self):
        # Close the cursor and connection to so the server can allocate
        # bandwidth to other requests
        self._db_cur.close()
        self._db_connection.close()
