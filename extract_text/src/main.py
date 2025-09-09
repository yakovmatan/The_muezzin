from extract_text.src.consumer import Consumer
from extract_text.src.config import *

consumer = Consumer(TOPIC_SUB, index_name=INDEX_NAME, topic_pub=TOPIC_PUB)


def main():
    consumer.consume_messages()


if __name__ == '__main__':
    main()
