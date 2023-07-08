# rest-api-python

install library
1. for post api
    Flask: pip install Flask
    Confluent Kafka: pip install confluent-kafka

2. for get api
pip install flask mysql-connector-python
Redpanda Python client: pip install redpanda
MariaDB Python client: pip install mariadb

Docs from red panda
## Run the setup script to download and install the repo
curl -1sLf 'https://dl.redpanda.com/nzc4ZYQK3WRGd9sy/redpanda/cfg/setup/bash.deb.sh' | sudo -E bash && \
## Use apt to install redpanda
sudo apt install redpanda -y && \
## Start redpanda as a service 
sudo systemctl start redpanda

How to run the API?
1. pipenv shell --python 3.8
2. python3 post.py 
3. api:
a. send the data http://127.0.0.1:5000/send-data 
b  get the data http://127.0.0.1:5000/data  

