## NOTE -- Implement multi threading 

import sqlite3
import random, time
from sqlite3 import Error
import paho.mqtt.subscribe as subscribe

address = "./iotdash/db.sqlite3"

def est_conn(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn # return conn or NONE in case of failure

def insert_data(conn, data):
    cur = conn.cursor()
    cur.execute('INSERT INTO api_latestdata (temperature, humidity, timestamp) VALUES (?,?, CURRENT_TIMESTAMP);', data)
    conn.commit()
    return int(cur.lastrowid)

# def generate_data():
#     data= random.sample(range(0,99), 2)
#     return data

def loop():
    while(True):
        conn =est_conn(address)
        if conn:
            print("Listening for data.....")
            msg = subscribe.simple("iot", hostname="0.0.0.0")   # replace "0.0.0.0" with your local IP
            data = []
            msg.payload = msg.payload.decode("utf-8")
            print("payload=", msg.payload)
            count =0
            for letter in msg.payload:
                if letter==" ":
                    break
                else:
                    count+=1
            temperature=float(msg.payload[:count])
            humidity=float(msg.payload[count+1:])

            #print(temperature+ "and"+ humidity)
            data.append(temperature)
            data.append(humidity)
            print("trying to insert ", data)
            row_id = insert_data(conn,data)
            print("Inserted ", data," into row=", row_id)
            
        else:
            print("connection failed")
            break



if __name__=="__main__":
    loop()
    #cur.execute('SELECT * FROM polls_iot WHERE id=?', row_id)
        