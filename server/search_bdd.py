import mysql.connector
from mysql.connector import Error

def select_data(select_query):
    host_name = 'localhost'
    user_name = 'root'
    user_password = 'root'
    db_name = 'immobilier_recherche'
    try:
        connection = mysql.connector.connect(host=host_name,
                                             user=user_name,
                                             password=user_password,
                                             database=db_name,
                                             port=8889)
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute(select_query)
            results = cursor.fetchall()
            return results
        else:
            return None;
    except Error as e:
        print("Error while connecting to MySQL : ", e)
def select_data_price(select_query, parameters):
    host_name = 'localhost'
    user_name = 'root'
    user_password = 'root'
    db_name = 'immobilier_recherche'
    try:
        connection = mysql.connector.connect(host=host_name,
                                             user=user_name,
                                             password=user_password,
                                             database=db_name,
                                             port=8889)
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute(select_query, parameters)
            results = cursor.fetchall()
            return results
        else:
            return None;
    except Error as e:
        print("Error while connecting to MySQL : ", e)