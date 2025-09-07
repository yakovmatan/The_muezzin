from processing.src.consumer import Consumer

consumer = Consumer('podcasts', index_name='podcasts')

def main():
    consumer.publish_messages()


if __name__ == '__main__':
    main()
