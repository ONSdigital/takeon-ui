from configparser import ConfigParser

from config_files.config_test import ConfigTest
from config_files.database_credentials import DatabaseCredentials


def db_config(filename=ConfigTest.file_path('database.ini'), section='postgresql'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)
    # get aws rds credentials
    secret = DatabaseCredentials().get_secret()

    # get section, default to postgresql
    db = {}

    # Checks to see if section (postgresql) parser exists
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            if param[1] == 'bdduser':
                db[param[0]] = secret['user']
            elif param[1] == 'bddpassword':
                db[param[0]] = secret['password']
            else:
                db[param[0]] = param[1]

        # Returns an error if a parameter is called that is not listed in the initialization file
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db
