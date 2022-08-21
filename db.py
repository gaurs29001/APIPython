import pymongo
import mysql.connector as connection


# mongodb connection
def mongodb_conn(in_client):
    print(in_client)
    client = pymongo.MongoClient(in_client)
    print(client)
    return client


# mysql dbconnection
def mysql_conn(in_host, in_user, in_pswrd):
    mydb = connection.connect(host=in_host, user=in_user, passwd=in_pswrd)
    return mydb


# mysql db operation
def mysql_exec(in_query, in_db, db_op):
    try:
        cursor = in_db.cursor(dictionary=True)
        cursor.execute(in_query)
        if db_op == 'SELECT':
            return cursor.fetchall()
    finally:
        in_db.commit()
        cursor.close()


# mongodb operation
def mongodb_exec(in_client, in_db, in_collctn):
    database = in_client[in_db]
    collection = database[in_collctn]
    return collection
