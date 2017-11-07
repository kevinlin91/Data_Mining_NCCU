from flask import Flask, jsonify, render_template, request
import sqlite3

  
app = Flask(__name__)
app.config.from_object('config')

@app.route("/")
def hello():    
    return "Hello World!"

@app.route("/dataapi")
def dateapi():
    return jsonify(test=1,test2=2)

@app.route("/get_irisdata")
def get_irisdata():
    conn = sqlite3.connect('../sqlite_example/iris.db')
    cursor = conn.cursor()
    data = cursor.execute("SELECT * FROM IRIS")
    result = list()
    for row in data:
        result.append( {'sepal_length':row[1], 'sepal_width':row[2], 'petal_length':row[3], 'petal_width':row[4], 'species':row[5]} )
    cursor.close()
    conn.close()
    return jsonify(result)

@app.route("/get_irisdata/<data_number>")
def get_irisdata_by_number(data_number):
    conn = sqlite3.connect('../sqlite_example/iris.db')
    cursor = conn.cursor()
    data = cursor.execute("SELECT * FROM IRIS WHERE ID=%s" % (data_number))
    result = list()
    for row in data:
        result.append( {'sepal_length':row[1], 'sepal_width':row[2], 'petal_length':row[3], 'petal_width':row[4], 'species':row[5]} )
    cursor.close()
    conn.close()
    return jsonify(result)

app.route('/send_data',method=['GET'])
def send_data():
    if request.method =='GET':
          
        return render_template

app.route('/show_data')
def show_data():
    return render_template('show_data.html')

if __name__=='__main__':
    app.run()
