from flask import Flask, request, jsonify
import db
app = Flask(__name__)


@app.route('/testfun',methods=['GET'])
def test():
    get_name = request.args.get("get_name")
    mobile = request.args.get("mobile")
    mail_id = request.args.get("mail")
    return "hello test function {} {} {}".format(get_name, mobile, mail_id)

@app.route('/testdb')
def test_db():
    table = request.args.get("table")
    in_host = 'localhost'
    in_user = 'root'
    in_pswrd = ''
    in_db = db.mysql_conn(in_host, in_user, in_pswrd)
    if in_db != None:
        query = "select sno, firstname, lastname, email, Date_of_Birth from {}".format(table)
        print(query)
        record = db.mysql_exec(query, in_db, 'SELECT')
        print(record)
        response = jsonify(str(record))
        response.status_code = 200
        return response


if __name__ == "__main__":
    app.run()