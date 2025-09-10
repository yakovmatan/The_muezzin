from services.processing.src.consumer import ConsumerManager
from services.processing.src.config import *

consumer = ConsumerManager(TOPIC_SUB, topic_pub=TOPIC_PUB, index_name=INDEX_NAME)


def main():
    consumer.consume_messages()


if __name__ == '__main__':
    main()
