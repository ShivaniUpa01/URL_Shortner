import json
import sys
from django.db import connections
from . import database_file
# from . import db_queries
from . import hash_algo_process
import logging
import validators

long_url = "https://docs.docker.com/desktop/install/mac-install/#:~:text=Double%2Dclick%20Docker.dmg%20to," \
           "Applications%20folder%20to%20start%20Docker."
short_url = '2eb9ac'


def read_configs(filepath):
    with open(filepath, 'r') as file:
        config_data = json.load(file)
    return config_data


def validate_url(url):
    if validators.url(url):
        return True
    else:
        raise Exception("URL not valid")


def convert_long_to_short_url(db_connector, long_url):
    # TODO:  Do validation of long url first if correct then only proceed.
    try:
        if validate_url(long_url):
            short = hash_algo_process.url_shortner_url_hash_algo(long_url)
            database_file.insert_data_in_url_mapping(db_connector, short, long_url)
            return short
    except Exception:
        return "Not a Valid URL"


def convert_short_to_long_url(connection, short_url):
    # TODO:  Do validation if the URL exist of not.
    try:
        if len(short_url) < 20 or database_file.select_data_in_url_mapping(connection, short_url):
            long = database_file.select_data_in_url_mapping(connection, short_url)
            return long
    except Exception:
        return "Short url is not present"



def setup_logging():
    # create a logger

    logger = logging.getLogger('urlshorter')
    #set logger level
    logger.setLevel(logging.INFO)

    handler = logging.FileHandler('/home/shivani/Url_shortner/venv/urlshortner/mylog.log')
    # create a logging format
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)


# if __name__ == "__main__":
#     # Reading configuration from config file
#     setup_logging()
#
#     try:
#         print(validate_url("https:/suraj.com"))
#     except Exception as e:
#         logging.error("Invalid URL tried %s", e)
#         print("Invalid URL exception")
#
#     print("After validation function call")
#
#     configs = read_configs("venv/urlshortner/config.json")

    # Creating database connection we automatically connected by django server
    # connection = database_file.database_connection(configs['host'], configs['db_user'], configs['db_pass'],
    #                                                configs["database"])

    # Setup all the resources here


# Get the default database connection
#     connection = connections['default']
#
#     # Long to Short URL convertion
#     result_short = convert_long_to_short_url(connection, long_url)
#     result_long = convert_short_to_long_url(connection, short_url)
#     connection.close()
#
#     print(result_short)
#     print(result_long)
