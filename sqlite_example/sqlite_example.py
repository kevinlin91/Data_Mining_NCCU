import sqlite3
import csv
import os.path
def load_data(path='./iris_data.csv'):
    iris = list()
    with open('./iris_data.csv','r') as f:
        for line in f.readlines()[1:]:
            iris.append(line.rstrip().split(','))
    return iris

def connect_db(path=''):
    conn = sqlite3.connect('iris.db')
    return conn

def create_table(cursor):
    cursor.execute('''CREATE TABLE IRIS
                        ( ID           INTEGER   PRIMARY KEY    AUTOINCREMENT,
                          SEPAL_LENGTH REAL                 NOT NULL,
                          SEPAL_WIDTH  REAL                 NOT NULL,
                          PETAL_LENGTH REAL                 NOT NULL,
                          PETAL_WIDTH  REAL                 NOT NULL,
                          SPECIES      CHAR(50)             NOT NULL);''')
    pass

def insert_item(sepal_length, sepal_width, petal_length, petal_width, species, cursor):
    command = "INSERT INTO IRIS (SEPAL_LENGTH, SEPAL_WIDTH, PETAL_LENGTH, PETAL_WIDTH, SPECIES) VALUES (%f, %f, %f, %f, \'%s\');" % (sepal_length, sepal_width, petal_length, petal_width, species)
    cursor.execute(command)

    pass


if __name__=="__main__":
    data = load_data()
    if(os.path.isfile('./iris.db')):
       conn = connect_db()
    else:
       conn = connect_db()
       create_table(conn.cursor())
    try:
        for items in data:
            insert_item(float(items[0]),float(items[1]),float(items[2]),float(items[3]),items[4],conn.cursor())
    except:
        print items
    conn.cursor().close()
    conn.commit()
    conn.close()   

    
        
    
            
