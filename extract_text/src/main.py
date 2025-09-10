from extract_text.src.consumer import ConsumerManager
from extract_text.src.config import *

consumer = ConsumerManager(TOPIC_SUB, index_name=INDEX_NAME)


def main():
    consumer.consume_messages()


if __name__ == '__main__':
    main()
