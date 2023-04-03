# sensor_streaming_data_pipeline
A Project on sensor streaming data pipeline setup with Kafka on confluent platform.

This repo help us to know how to publish and consume data to and from kafka confluent in json format.

Step1: Create  a conda environment
```
conda create -p venv python==3.8 -y
```

Step2:
```
conda activate venv/
```
Step3:
```
pip install -r requirements.txt
```


Cluster Environment Variable
```
API_KEY
API_SECRET_KEY
BOOTSTRAP_SERVER
```

Schema related Environment Variable
```
SCHEMA_REGISTRY_API_KEY
SCHEMA_REGISTRY_API_SECRET
ENDPOINT_SCHEMA_URL
```
Data base related Environment Variable
```
MONGO_DB_URL
```

set the above environment variables .

run the produce_main.py to produce the data into confluent kafka topic.

run the consumer_main.py to consume the data in parallel from kafka topic.