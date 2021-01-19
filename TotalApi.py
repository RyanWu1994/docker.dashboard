from flask_sqlalchemy import SQLAlchemy
from flask import Flask,jsonify,request,make_response
from flask_cors import cross_origin,CORS

# 設定DB連線
DB_host = "0.0.0.0"
DB_user = "ryan"
DB_passwd = "Aa123456"
DB_port = "3306"
DB_name = "solar"

app = Flask(__name__)
CORS(app, resources=r'/*', supports_credentials=True)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://" + DB_user + ":"+ DB_passwd +"@"+ DB_host +":"+ DB_port +"/"+ DB_name
db = SQLAlchemy(app)

# 电信 Telecom
@app.route('/TotalApi', methods=['GET'])
def TotalApi():

    sql_cmd = """
        SELECT * from test
        """
    query_data = db.engine.execute(sql_cmd)
    date = query_data.fetchall()
    
    response = jsonify({'result': [dict(row) for row in date]})

    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = '*'
    response.headers['Access-Control-Allow-Headers'] = '*'

    return response


if __name__ == "__main__":
    app.run( host='127.0.0.1',port=5000, debug=True)
