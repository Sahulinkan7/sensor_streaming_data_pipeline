
from src.kafka_producer.json_producer import produce_data_using_file
from src.constant import SAMPLE_DIR
import os

if __name__=='__main__':
    
    available_topics=os.listdir(SAMPLE_DIR)
    print(available_topics)
    for topic in available_topics:
        sample_topic_data_dir=os.path.join(SAMPLE_DIR,topic)
        sample_file_path=os.path.join(sample_topic_data_dir,os.listdir(sample_topic_data_dir)[0])
        produce_data_using_file(topic_name=topic,file_path=sample_file_path)