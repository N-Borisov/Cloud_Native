from flask import Flask
from flask import json
from flask import Flask,render_template, request
from flask_mysqldb import MySQL
from dotenv import load_dotenv
from os import environ 
import logging

app = Flask(__name__)

load_dotenv()

app.config['MYSQL_HOST'] = 'mysql.app.svc.cluster.local'
app.config['MYSQL_USER'] = os.getenv('MYSQL_DATABASE_USER')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_DATABASE_PASSWORD')

mysql = MySQL(app)

@app.route('/status')
def healthcheck():
    response = app.response_class(
            response=json.dumps({"result":"OK - healthy"}),
            status=200,
            mimetype='application/json'
    )
    app.logger.info('Status request successfull')
    app.logger.debug('DEBUG message')
    return response

@app.route('/metrics')
def metrics():
    response = app.response_class(
            response=json.dumps({"status":"success","code":0,"data":{"UserCount":140,"UserCountActive":23}}),
            status=200,
            mimetype='application/json'
    )
    app.logger.info('Metrics request successfull')
    return response

@app.route("/")
def hello():
    app.logger.info('Main request successfull')

    return "Cloud Native - version: 1"

@app.route('/version')
def version():
        cur = mysql.connection.cursor()
        cur.execute("SELECT VERSION()")
        rv = cur.fetchall()
        return f'You are running MYSQL Database version: {str(rv)}'


if __name__ == "__main__":
    ## stream logs to a file
    logging.basicConfig(filename='app.log',level=logging.DEBUG)
    
    app.run(host='0.0.0.0')