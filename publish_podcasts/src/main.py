import time

from publish_podcasts.src.produser import Manager
from publish_podcasts.src.config import *
manager = Manager()

def main():
    manager.publish_messages(TOPIC)

if __name__ == '__main__':
    main()