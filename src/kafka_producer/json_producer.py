from src.entity.generic import Generic,instance_to_dict
from confluent_kafka import Producer
from src.kafka_config import schema_config,sasl_conf
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.serialization import StringSerializer,SerializationContext,MessageField
from confluent_kafka.schema_registry.json_schema import JSONSerializer
import pandas as pd
from uuid import uuid4
from src.kafka_logger import logging
from typing import List

def delivery_report(err, msg):
    """
    Reports the success or failure of a message delivery.
    Args:
        err (KafkaError): The error that occurred on None on success.
        msg (Message): The message that was produced or failed.
        
    """
    if err is not None:
        logging.info(f"Delivery failed for User record {msg.key()}: {err}")
        return
    logging.info(f'User record {msg.key()} successfully produced to {msg.topic()} [{msg.partition()}] at offset {msg.offset()}')



def produce_data_using_file(topic_name,file_path):
    schema_str=Generic.get_schema_to_produce_consume_data(file_path=file_path)
    schema_registry_conf=schema_config()
    schema_registry_client=SchemaRegistryClient(schema_registry_conf)
    string_serializer=StringSerializer('utf_8')
    json_serializer=JSONSerializer(schema_str,schema_registry_client,instance_to_dict)
    producer=Producer(sasl_conf())
    print(f"Producing user records to the topic {topic_name}")
    
    producer.poll(0.0)
    try:
        for instance in Generic.get_object(file_path=file_path):
            print(instance)
            logging.info(f"Topic: {topic_name} file_path : {instance.to_dict()}")
            producer.produce(topic=topic_name,
                            key=string_serializer(str(uuid4()),instance.to_dict()),
                            value=json_serializer(instance,SerializationContext(topic_name,MessageField.VALUE)),
                            on_delivery=delivery_report)
            print("\nFlushing records...")
            producer.flush()
    except KeyboardInterrupt:
        pass
    except ValueError:
        print("Invalid input .")
        
    