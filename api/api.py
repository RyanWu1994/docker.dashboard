from flask_sqlalchemy import SQLAlchemy
from flask import Flask,jsonify,request,make_response
from flask_cors import cross_origin,CORS
import os

# 設定DB連線
DB_host = os.environ['MYSQL_HOST']
DB_user = os.environ["MYSQL_USER"]
DB_passwd = os.environ['MYSQL_PASSWORD']
DB_port = os.environ['MYSQL_PORT']
DB_name = os.environ["MYSQL_DB"]

app = Flask(__name__)
CORS(app, resources=r'/*', supports_credentials=True)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://" + DB_user + ":"+ DB_passwd +"@"+ DB_host +":"+ DB_port +"/"+ DB_name
db = SQLAlchemy(app)

@app.route('/api', methods=['GET'])
def TotalApi():

    sql_cmd = """
        SELECT * from dashboard;
        """
    query_data = db.engine.execute(sql_cmd)
    date = query_data.fetchall()
    
    response = jsonify({'result': [dict(row) for row in date]})

    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = '*'
    response.headers['Access-Control-Allow-Headers'] = '*'

    return response

if __name__ == "__main__":
    app.run( host='0.0.0.0',port=5000, debug=True)
