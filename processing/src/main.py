import time

from processing.src.consumer import Consumer
from processing.src.config import *
consumer = Consumer(TOPIC, index_name=INDEX_NAME)

def main():
    time.sleep(100)
    consumer.publish_messages()


if __name__ == '__main__':
    main()
