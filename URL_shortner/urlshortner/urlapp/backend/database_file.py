import mysql.connector
import logging as log
from . import db_queries


# def database_connection(host_name, user_name, user_password, database_name):
#     mydb = mysql.connector.connect(host=host_name,
#                                    user=user_name,
#                                    password=user_password,
#                                    database=database_name)
#     log.info("Database Connection Established")
#     print("Database Connection Established")
#     return mydb


# Setup resources of database if not already exist
def setup_database(db_connector):
    create_table(db_connector, db_queries.create_table_url_mapping)


def create_table(db_connector, query):
    cursor = db_connector.cursor()
    cursor.execute(query)
    db_connector.commit()  # permanent change
    cursor.close()


def insert_data_in_url_mapping(db_connector, short_url, long_url):
    cursor = db_connector.cursor()
    data = (short_url, long_url)
    cursor.execute(db_queries.insert_data_url_mapping, data)
    db_connector.commit()
    cursor.close()


def select_data_in_url_mapping(db_connector, test_url):
    cursor = db_connector.cursor()
    # test = test_url
    cursor.execute(db_queries.select_data_url_mapping, (test_url, ))
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            column = row[0]
    else:
        column = "No data found"
    db_connector.commit()
    cursor.close()
    return column

