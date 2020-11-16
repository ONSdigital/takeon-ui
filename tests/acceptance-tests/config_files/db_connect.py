import os
import subprocess

import psycopg2
from pandas import read_sql_query
from config_files import db_config, aws_config
from config_files.config_test import ConfigTest


class DBConnect:

    def __init__(self):
        # Obtain the configuration parameters
        params = db_config.db_config()
        # Connect to the PostgreSQL database
        self._db_connection = psycopg2.connect(**params)
        # Establish a connection to the database by creating a cursor object
        self._db_cur = self._db_connection.cursor()

    def db_create_pandas_table(self, sql_query):
        # A function that takes in a PostgreSQL query and outputs a pandas data frame
        table = read_sql_query(sql_query, self._db_connection)
        return table

    def db_select_query(self, query):
        # Utilize the db_create_pandas_table function to create a Pandas data frame
        # Store the data as a variable
        self.db_create_pandas_table(query)

    def db_close(self):
        # Close the cursor and connection to so the server can allocate
        # bandwidth to other requests
        self._db_cur.close()
        self._db_connection.close()
