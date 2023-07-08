# Library for post api
from flask import Flask, request
from kafka import KafkaProducer

# Library for get api
from flask import Flask, request, jsonify
import mysql.connector
# from redpanda import RedpandaClient
import redpanda


app = Flask(__name__)

KafkaProducer(bootstrap_servers=['localhost:5000'],
              api_version=(0,11,5),
              value_serializer=lambda x: dumps(x).encode('utf-8'))

@app.route('/send-data', methods=['POST'])
def send_data():
    data = request.get_json()  # JSON data
    topic = 'Send meesage to Redpanda'
    producer.send(topic, value=data)
    return 'Data sent to Redpanda!'


# api get
@app.route('/data', methods=['GET'])
def get_data():
    # Connect to Redpanda and retrieve data
    #redpanda_client = RedpandaClient('<redpanda_host>', '<redpanda_port>')
    redpanda_client = RedpandaClient('testing', '6000')
    data = redpanda_client.retrieve_data()

    # Connect to MariaDB
    db_connection = mysql.connector.connect(
        host='testing',
        user='testing',
        password='123testing',
        database='python'
    )
    cursor = db_connection.cursor()

    # Insert data into MariaDB
    insert_query = "INSERT INTO consumer (id, message) VALUES (%1, %hellodata)"  # Adjust column names and table name
    for item in data:
        values = (item['id'], item['message'])  # Adjust column names
        cursor.execute(insert_query, values)

    db_connection.commit()
    cursor.close()
    db_connection.close()

    return jsonify({'message': 'Data saved successfully'})

if __name__ == '__main__':
    app.run(debug=True)