from . import constants

create_table_url_mapping = "CREATE TABLE  if not exists " + constants.table_name_url_mapping + "(url_id int " \
                                                                                               "auto_increment primary " \
                                                                                               "key, short_url " \
                                                                                               "varchar(12), long_url " \
                                                                                               "text UNIQUE)"

insert_data_url_mapping = "insert into " + constants.table_name_url_mapping + "(short_url, long_url) values(%s, %s)"

select_data_url_mapping = "Select long_url from " + constants.table_name_url_mapping + " where short_url = %s"
