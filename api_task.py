"""
1. write program to insert a record in sql table via api
2. write program to update a record in sql table via api
3. write program to fetch a record in sql table via api
4. write program to delete a record in sql table via api
5. All above questions for mongodb
"""

from flask import Flask, request, jsonify
import db


#Flask application
myapp = Flask(__name__)


@myapp.route('/mysql/insert', methods=['GET', 'POST'])
def mysql_insert():
    if request.method == 'POST':
        in_host = request.json['host']
        in_user = request.json['user']
        in_pswrd = request.json['password']
        in_db = db.mysql_conn(in_host, in_user, in_pswrd)
        if in_db != None:
            in_sno = request.json['sno']
            in_firstname = request.json['firstname']
            in_lastname = request.json['lastname']
            in_email = request.json['email']
            in_dob = request.json['DOB']
            query = f"insert into ineuron_task.student_detail (sno, firstname, lastname, email, Date_of_Birth) values ({in_sno}, '{in_firstname}', '{in_lastname}', '{in_email}', '{in_dob}')"
            db.mysql_exec(query, in_db, '')
            response = jsonify('Record added')
            response.status_code = 200
            return response


@myapp.route('/mysql/delete/', methods=['DELETE'])
def mysql_delete():
    if request.method == 'DELETE':
        in_sno = request.json['sno']
        in_host = request.json['host']
        in_user = request.json['user']
        in_pswrd = request.json['password']
        in_db = db.mysql_conn(in_host, in_user, in_pswrd)
        if in_db != None:
            query = f"delete from ineuron_task.student_detail where sno = {in_sno}"
            print(query)
            db.mysql_exec(query, in_db, '')
            response = jsonify('Record deleted')
            response.status_code = 200
            return response


@myapp.route('/mysql/update/', methods=['PUT'])
def mysql_update():
    if request.method == 'PUT':
        in_host = request.json['host']
        in_user = request.json['user']
        in_pswrd = request.json['password']
        in_db = db.mysql_conn(in_host, in_user, in_pswrd)
        if in_db != None:
            in_sno = request.json['sno']
            in_firstname = request.json['firstname']
            in_lastname = request.json['lastname']
            in_email = request.json['email']
            in_dob = request.json['DOB']
            query = f"update ineuron_task.student_detail set firstname = '{in_firstname}', lastname = '{in_lastname}', email ='{in_email}', Date_of_Birth ='{in_dob}' where sno = {in_sno}"
            db.mysql_exec(query, in_db, '')
            response = jsonify('Record updated')
            response.status_code = 200
            return response


@myapp.route('/mysql/select', methods=['POST'])
def mysql_select():
    if request.method == 'POST':
        in_host = request.json['host']
        in_user = request.json['user']
        in_pswrd = request.json['password']
        in_db = db.mysql_conn(in_host, in_user, in_pswrd)
        if in_db != None:
            query = f"select sno, firstname, lastname, email, Date_of_Birth from ineuron_task.student_detail"
            #print(query)
            record = db.mysql_exec(query, in_db, 'SELECT')
            #print(record)
            response = jsonify(record)
            response.status_code = 200
            return response


@myapp.route('/mongodb/insert', methods=['GET', 'POST'])
def mongodb_insert():
    if request.method == 'POST':
        in_client = request.json['client']
        in_db = request.json['database']
        in_collctn = request.json['collection']
        in_json = request.json['in_json']
        mongo_client = db.mongodb_conn(in_client)
        mongo_collection = db.mongodb_exec(mongo_client, in_db, in_collctn)
        mongo_collection.insert_many(in_json)
        response = jsonify('Record added')
        response.status_code = 200
        return response


@myapp.route('/mongodb/delete', methods=['DELETE'])
def mongodb_delete():
    if request.method == 'DELETE':
        in_client = request.json['client']
        in_db = request.json['database']
        in_collctn = request.json['collection']
        in_sno = request.json['sno']
        mongo_client = db.mongodb_conn(in_client)
        mongo_collection = db.mongodb_exec(mongo_client, in_db, in_collctn)
        print(mongo_collection)
        mongo_collection.delete_one({"sno": in_sno})
        response = jsonify('Record deleted')
        response.status_code = 200
        return response


@myapp.route('/mongodb/select', methods=['POST'])
def mongodb_select():
    if request.method == 'POST':
        in_client = request.json['client']
        in_db = request.json['database']
        in_collctn = request.json['collection']
        in_sno = request.json['sno']
        mongo_client = db.mongodb_conn(in_client)
        mongo_collection = db.mongodb_exec(mongo_client, in_db, in_collctn)
        record = mongo_collection.find({"sno": in_sno})
        result = []
        for i in record:
            result.append(str(i))
        response = jsonify(result)
        response.status_code = 200
        return response


@myapp.route('/mongodb/update', methods=['PUT'])
def mongodb_update():
    if request.method == 'PUT':
        in_client = request.json['client']
        in_db = request.json['database']
        in_collctn = request.json['collection']
        in_sno = request.json['sno']
        in_firstname = request.json['firstname']
        in_lastname = request.json['lastname']
        in_email = request.json['email']
        in_dob = request.json['DOB']
        mongo_client = db.mongodb_conn(in_client)
        mongo_collection = db.mongodb_exec(mongo_client, in_db, in_collctn)
        mongo_collection.update_one({"sno": in_sno}, {'$set': {"firstname": in_firstname, "lastname": in_lastname, "email": in_email, "DOB": in_dob}})
        response = jsonify('Record updated')
        response.status_code = 200
        return response


if __name__ == '__main__':
    myapp.run()