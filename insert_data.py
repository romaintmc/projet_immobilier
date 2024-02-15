import mysql.connector
import pandas as pd
from mysql.connector import Error
import server.search as sc

PATH = '/Users/romaintmc/Desktop/prix_immobilier_fictif.csv'

host_name = 'localhost'
user_name = 'root'
user_password = 'root'
db_name = 'immobilier_recherche'


def insert_data(host_name, user_name, user_password, db_name, insert_query):
    try:
        connection = mysql.connector.connect(host=host_name,
                                             user=user_name,
                                             password=user_password,
                                             database=db_name,
                                             port=8889)
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute(insert_query)
            connection.commit()
            print("Data inserted successfully")
    except Error as e:
        print("Error while connecting to MySQL", e)

if __name__ == '__main__':
    df = pd.read_csv(PATH, low_memory=False, sep=',')

    for index, row in df.iterrows():
        ville = row['Ville']
        quartier = row['Quartier']
        prix = row['Prix']
        insert_query = 'INSERT INTO ville_quartier (nom, nom_ville, prix) VALUES ("{0}", "{1}", {2});'.format(quartier,ville,prix)
        print(insert_query)
        insert_data(host_name, user_name, user_password, db_name, insert_query)
